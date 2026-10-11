# Lab02 - Bài 7: Kiểm tra chu trình trong DFS

## Nội dung
- `05_Maze_Example_Cycle_checking_Bai7_Hoan_thien.ipynb`: giữ nguyên 12 cell gốc và bổ sung các cell Code/Markdown để hoàn thiện yêu cầu.
- `tree_search_solution.py`: **cài đặt minh họa độc lập**, không phải mã gốc chưa được công bố của giảng viên. Có ba phương án frontier_option=3/2/1 với nhật ký thống kê.
- `maze_helper.py`, `open_maze.txt`: các tài nguyên để chạy notebook.
- `ket_qua_bai7_cycle_checking.csv`: bảng so sánh, `frontier_option_*.png`: đồ thị frontier.

## Hướng dẫn
1. Giải nén tất cả file trong cùng thư mục.
2. Cài `numpy`, `pandas`, `matplotlib`, `ipython`, `ipykernel`, `nbformat` (nếu thiếu).
3. Mở notebook bằng VS Code hoặc Jupyter, chạy Restart & Run All.
4. Các cell gốc có animation; máy yếu có thể chỉ chạy các cell Bài 7 bổ sung để giảm thời gian hiển thị.

## Phân biệt thống kê
- `iterations`: số lần lấy nút ra khỏi stack, kể cả nút bị loại do lặp trên đường đi.
- `expanded`: số lần mở rộng hợp lệ.
- `repeated_expansions`: số lượt mở rộng vượt quá số trạng thái phân biệt.
- `max_frontier`: số entry tối đa tại một thời điểm.
- `max_duplicate_entries`: số entry bản sao tại một thời điểm.

Phương án 1/2 có thể kết thúc vì giới hạn 500, đây là hiện tượng lặp nhiều, không phải bằng chứng lặp vô hạn trong mê cung hữu hạn.
