"""Independent educational implementation for Lab02 searching.

API-compatible with the example notebooks' publicly visible function calls.
This is NOT the unpublished original tree_search_solution.py by the author.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from itertools import count
import heapq
import random as _random
from typing import Optional
import numpy as np
import maze_helper as mh

_ORDER = 'NESW'
_RANDOM = False
_STEPS = {'N':(-1,0), 'E':(0,1), 'S':(1,0), 'W':(0,-1)}
heuristic = None

@dataclass(eq=False)
class Node:
    pos: tuple
    parent: Optional['Node']
    action: Optional[str]
    cost: int
    depth: int = 0

    def get_path_from_root(self):
        path, current = [], self
        while current is not None:
            path.append(current)
            current = current.parent
        return path[::-1]


def set_order(order='NESW', random=False):
    """Order is the *push* order; DFS pop order is its reverse."""
    global _ORDER, _RANDOM
    if random:
        _RANDOM = True
    else:
        order = str(order).upper()
        if len(order) != 4 or set(order) != set('NESW'):
            raise ValueError('order must be a permutation of NESW')
        _ORDER = order
        _RANDOM = False


def available(maze, pos):
    order = list(_ORDER)
    if _RANDOM:
        _random.shuffle(order)
    for direction in order:
        dr, dc = _STEPS[direction]
        n = (pos[0] + dr, pos[1] + dc)
        if 0 <= n[0] < maze.shape[0] and 0 <= n[1] < maze.shape[1] and maze[n] != 'X':
            yield direction, n


def manhattan(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


def _path_nodes(node):
    return node.get_path_from_root() if node is not None else []


def _result(node, expanded, max_frontier, max_depth, snapshots, expanded_order, frontier_trace, stopped=False):
    nodes = _path_nodes(node)
    return {
        'path': [n.pos for n in nodes] if node is not None else None,
        'actions': [n.action for n in nodes[1:]] if node is not None else [],
        'path_cost': node.cost if node is not None else None,
        'reached': set(expanded_order),
        'n_expanded': expanded,
        'nodes_expanded': expanded,
        'max_frontier': max_frontier,
        'max_depth': max_depth,
        'trace': frontier_trace,
        'expanded_order': expanded_order,
        'snapshots': snapshots,
        'stopped_by_limit': stopped,
    }


def _snapshot(maze, expanded_nodes, frontier_positions, node, snapshots, animation, counter):
    if not animation:
        return
    # Cap displayed frames to avoid excessive memory and notebook HTML size.
    if len(snapshots) >= 70 or (counter > 15 and counter % 8 != 0):
        return
    marked = np.copy(maze)
    for p in expanded_nodes:
        if marked[p] == ' ':
            marked[p] = '.'
    for p in frontier_positions:
        if marked[p] == ' ':
            marked[p] = 'F'
    if node and marked[node.pos] == ' ':
        marked[node.pos] = '.'
    snapshots.append(marked)


def _finish_animation(result, maze):
    snaps = result['snapshots']
    end = np.copy(maze)
    for p in result['reached']:
        if end[p] == ' ': end[p] = '.'
    if result['path']:
        for p in result['path'][1:-1]:
            if end[p] == ' ' or end[p] == '.': end[p] = 'P'
    snaps.append(end)
    result['maze_anim'] = snaps if snaps else [end]
    return result


def best_first_search(maze, strategy='BFS', debug=False, vis=False, animation=False, W=1.0, max_tries=100000):
    """Queue BFS, graph DFS, greedy BF, A* and weighted A*.

    Reached for BFS is marked on discovery; expanded counts actual pops
    resulting in successor generation (not the final goal node).
    """
    maze = np.asarray(maze)
    start, goal = mh.find_pos(maze, 'S'), mh.find_pos(maze, 'G')
    mode = strategy.upper().replace(' ', '')
    if mode not in ('BFS','DFS','GBFS','A*'):
        raise ValueError('Unknown strategy '+strategy)
    root = Node(start, None, None, 0, 0)
    q = deque([root])
    heap = []
    ticket = count()
    if mode in ('GBFS','A*'):
        heapq.heappush(heap, (0.0, next(ticket), root))
    reached = {start}
    best_g = {start: 0}
    expanded_order, trace, snaps = [], [], []
    max_frontier, max_depth = 1, 0
    found = None
    stopped = False
    while (heap if mode in ('GBFS','A*') else q):
        if len(expanded_order) >= max_tries:
            stopped = True
            break
        if mode in ('GBFS','A*'):
            _, _, node = heapq.heappop(heap)
            if node.cost > best_g[node.pos]:
                continue
        elif mode == 'BFS':
            node = q.popleft()
        else:
            node = q.pop()
        if node.pos == goal:
            found = node
            break
        expanded_order.append(node.pos)
        max_depth = max(max_depth,node.depth)
        for action, pos in available(maze, node.pos):
            cost = node.cost + 1
            if mode in ('BFS','DFS'):
                if pos in reached: continue
                reached.add(pos)
            else:
                if cost >= best_g.get(pos, float('inf')): continue
                best_g[pos] = cost
            child = Node(pos,node,action,cost,node.depth+1)
            if mode in ('GBFS','A*'):
                h = (heuristic or manhattan)(pos,goal)
                priority = h if mode=='GBFS' else cost+W*h
                # negative order index favours most recently generated item on ties
                heapq.heappush(heap,(priority, -next(ticket), child))
            else:
                q.append(child)
        curr_frontier = [entry[-1].pos for entry in heap] if mode in ('GBFS','A*') else [n.pos for n in q]
        max_frontier = max(max_frontier,len(curr_frontier))
        if len(trace) < 2000:
            trace.append({'step':len(expanded_order), 'expanded':node.pos,
                          'frontier_size':len(curr_frontier), 'frontier':tuple(curr_frontier[:25])})
        _snapshot(maze, expanded_order,curr_frontier,node,snaps,animation,len(expanded_order))
    result = _result(found,len(expanded_order),max_frontier,max_depth,snaps,expanded_order,trace,stopped)
    if animation:
        _finish_animation(result,maze)
    return result


def DFS(maze, vis=False, max_tries=100000, debug_reached=False, check_cycle=True,
        frontier_option=1, limit=None, animation=False, **kwargs):
    """Illustrative DFS cycle-checking methods described in the class notebook.

    frontier_option=3: check current root-to-node path only.
    frontier_option=2: check path and reject duplicate entries already in stack.
    frontier_option=1: check path and move existing entry to top of stack.

    The author's unpublished implementation is NOT reproduced here: this is
    a transparent, independently implemented educational approximation.
    """
    import time
    if frontier_option not in (1, 2, 3):
        raise ValueError('frontier_option must be one of 1, 2, 3')
    maze = np.asarray(maze)
    start, goal = mh.find_pos(maze, 'S'), mh.find_pos(maze, 'G')
    stack = [Node(start, None, None, 0, 0)]
    expanded_order, popped_order, trace, snapshots = [], [], [], []
    repeated_pop=0
    cycle_pruned=0
    in_frontier_skipped=0
    promoted=0
    max_frontier, max_depth, max_duplicate_entries = 1, 0, 0
    found, stopped = None, False
    began = time.perf_counter()
    iterations = 0
    while stack:
        if iterations >= max_tries:
            stopped = True
            break
        node = stack.pop()
        iterations += 1
        popped_order.append(node.pos)
        # Explicit path check, performed on extraction as described by notebook.
        current = node.parent
        ancestor_positions = set()
        while current is not None:
            ancestor_positions.add(current.pos)
            current = current.parent
        if check_cycle and node.pos in ancestor_positions:
            cycle_pruned += 1
            continue
        if node.pos == goal:
            found = node
            break
        expanded_order.append(node.pos)
        max_depth = max(max_depth, node.depth)
        if limit is None or node.depth < limit:
            for action, nxt in available(maze, node.pos):
                child = Node(nxt, node, action, node.cost + 1, node.depth + 1)
                if frontier_option in (1, 2):
                    duplicate_idx = next((j for j, e in enumerate(stack) if e.pos == nxt), None)
                    if duplicate_idx is not None:
                        if frontier_option == 2:
                            in_frontier_skipped += 1
                            continue
                        # Move original entry to top; keep its stored ancestry and cost.
                        prior = stack.pop(duplicate_idx)
                        stack.append(child)  # update parent to reflect newest discovery
                        promoted += 1
                        continue
                stack.append(child)
        from collections import Counter
        duplicates = sum(c-1 for c in Counter(n.pos for n in stack).values() if c > 1)
        max_duplicate_entries = max(max_duplicate_entries, duplicates)
        max_frontier = max(max_frontier, len(stack))
        if len(trace) < 1000:
            trace.append({'step':iterations, 'expanded':node.pos,
                          'frontier_size':len(stack),
                          'frontier_duplicates':duplicates})
        # Keep a manageable subset of frames for the notebook HTML animation.
        _snapshot(maze, set(expanded_order), [n.pos for n in stack], node,
                  snapshots, animation, len(expanded_order))
    result = _result(found, len(expanded_order), max_frontier, max_depth,
                     snapshots, expanded_order, trace, stopped=stopped)
    result.update({'iterations': iterations, 'popped_order': popped_order,
                   'repeated_expansions':len(expanded_order)-len(set(expanded_order)),
                   'distinct_expanded':len(set(expanded_order)),
                   'cycle_pruned':cycle_pruned,
                   'frontier_skipped':in_frontier_skipped,
                   'frontier_promoted':promoted,
                   'max_duplicate_entries':max_duplicate_entries,
                   'frontier_leftover':len(stack),
                   'elapsed_ms':(time.perf_counter()-began)*1000,
                   'frontier_option':frontier_option})
    if animation:
        _finish_animation(result,maze)
    return result


def IDS(maze, frontier_option=2, max_tries=100000, vis=False, **kwargs):
    """Iterative deepening, depth-limited graph search with depth dominance.

    Each iteration retains only the shallowest discovered depth for a state,
    avoiding exponential revisits within a single depth limit.
    """
    maze=np.asarray(maze)
    start,goal=mh.find_pos(maze,'S'),mh.find_pos(maze,'G')
    state_bound=int(np.count_nonzero(maze != 'X'))
    total_expanded, max_frontier=0,0
    result=None
    for limit in range(state_bound):
        root=Node(start,None,None,0,0)
        stack=[root]
        best_depth={start:0}
        expanded_order=[]
        found=None
        while stack and total_expanded < max_tries:
            node=stack.pop()
            if node.depth > best_depth.get(node.pos,float('inf')):
                continue
            if node.pos==goal:
                found=node;break
            expanded_order.append(node.pos)
            total_expanded+=1
            if node.depth >= limit:continue
            for action,pos in available(maze,node.pos):
                new_depth=node.depth+1
                if new_depth >= best_depth.get(pos,float('inf')):
                    continue
                best_depth[pos]=new_depth
                stack.append(Node(pos,node,action,new_depth,new_depth))
            max_frontier=max(max_frontier,len(stack))
        result=_result(found,total_expanded,max_frontier,limit,[],expanded_order,[],total_expanded >= max_tries)
        if found is not None or total_expanded >= max_tries:
            break
    return result if result is not None else _result(None,0,0,0,[],[],[],True)


def min_index(xs):
    return xs.index(min(xs))


def show_maze(maze):
    return mh.show_maze(maze)


def show_path(maze,result):
    """Show summary, and draw the route using a separate copy of the maze."""
    if result['path'] is None:
        print('No solution found; expanded:',result['n_expanded'],
              '; terminated at max_tries:',result['stopped_by_limit'])
        return
    print('Path cost:',result['path_cost'],
          '| Expanded:',result['n_expanded'],
          '| Max frontier:',result['max_frontier'],
          '| Max depth:',result['max_depth'])
    print('Actions:', ''.join(result['actions']))
    display_maze=np.copy(maze)
    for pos in result['reached']:
        if display_maze[pos]==' ':display_maze[pos]='.'
    for pos in result['path'][1:-1]:
        if display_maze[pos] in ('.',' '):display_maze[pos]='P'
    mh.show_maze(display_maze)


def animate_maze(result):
    """Return a matplotlib animation compatible with the supplied maze_helper.py."""
    return mh.animate_maze(result)
