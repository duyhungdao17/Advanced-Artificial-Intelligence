# Lab02 - Bài 3: BFS và DFS

## Thành phần
- `02_Maze_Example_Bai3_Hoan_thien.ipynb`: giữ nguyên phần Code/Markdown gốc, thêm thí nghiệm BFS/DFS và giải thích bằng tiếng Việt.
- `03_Maze_Example_Animation_Bai3_Hoan_thien.ipynb`: giữ nguyên phần Code/Markdown gốc, thêm animation BFS/DFS và nhận xét.
- `tree_search_solution.py`: bản triển khai độc lập theo giao diện được hai notebook gốc sử dụng. **Không phải** bản mã nguồn chưa công bố của giảng viên/tác giả.
- `maze_helper.py`, 8 file `*_maze.txt`: tài liệu hỗ trợ đã cung cấp.
- `ket_qua_bai3.csv`: bảng thống kê BFS và DFS với thứ tự xác định.

## Cách chạy
1. Giải nén toàn bộ vào **cùng một thư mục**. Không tách notebook khỏi `.py` và `.txt`.
2. Mở từng `.ipynb` bằng Jupyter/VS Code/Google Colab với Python 3 đã có `numpy`, `matplotlib`, `pandas`, `ipython`, `ipykernel`.
3. Chạy **Restart & Run All**; các mục code nâng cao từ notebook gốc (IDS, GBFS, A*) vẫn được giữ để phục vụ bài tiếp theo.
4. Mục Bài 3 bổ sung ở cuối notebook dùng `small_maze.txt` làm ví dụ nhất quán.
5. Animation chỉ hiển thị các frame mẫu để tránh file quá nặng.

## Quy ước thực nghiệm
- `n_expanded`: số nút được lấy ra và mở rộng (không bao gồm thao tác kiểm tra nút đích).
- DFS có `check_cycle=True`: loại bỏ trạng thái có mặt trên **đường đi hiện tại**; khác với global visited set, nên có thể mở rộng lại một vị trí ở nhánh khác.
- Nghiệm DFS phụ thuộc thứ tự thêm trạng thái con, kết quả ngẫu nhiên đã được cố định seed để có thể tái lập.
- Nếu không quản lý chu trình, DFS có thể tốn thời gian lớn; `max_tries` là giới hạn thực nghiệm, không thuộc tính đầy đủ lý thuyết.
