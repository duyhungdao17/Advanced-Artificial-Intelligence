# LAB 02 - Bài 4: Depth-Limited DFS và IDS

## Cấu trúc
- `02_Maze_Example_Bai4_Hoan_thien.ipynb`: notebook 66 cells, bao gồm cả nội dung gốc, Bài 3 và 17 cells Bài 4.
- `tree_search_solution.py`: mã nguồn hỗ trợ độc lập tương thích API của ví dụ; KHÔNG PHẢI mã gốc chưa công bố của tác giả.
- `maze_helper.py`: tệp hỗ trợ hiển thị và đọc mê cung do bạn cung cấp.
- `*_maze.txt`: 8 mê cung. File large_maze đã chuẩn hóa tên từ large_maze(1).txt.
- `ket_qua_bai4_DLS_IDS.csv`: bảng chỉ số DLS và IDS; số lần lặp IDS từng mức.

## Chạy lại
1. Giải nén toàn bộ ZIP vào một thư mục.
2. Mở notebook trong VS Code / Jupyter.
3. Chọn `Restart & Run All` (chạy từ đầu đến cuối).
4. Đọc mục `BÀI 4` ở cuối notebook. Phần này lấy dữ liệu `small_maze.txt` riêng nên không bị ảnh hưởng bởi biến `maze` dùng trong so sánh thời gian ở phía trên.

## Quy ước thực nghiệm
- Hướng thêm nút vào stack: NESW. Stack LIFO sẽ lấy nút thêm sau trước.
- Đánh dấu chu trình theo đường đi tổ tiên hiện tại; không dùng tập reached toàn cục cắt bỏ đường đi khác.
- Đếm n_expanded khi nút sinh successor; không tính nút bị chặn tại limit hoặc nút đích.
- IDS chạy DLS độc lập cho từng L=0,1,... cho đến khi đạt đích.
- DLS trên small_maze: L=18 CUTOFF; L=19 FOUND/cost19; L=30 FOUND/cost29.
- IDS trên small_maze: 20 vòng DLS, 19 lần tăng limit, cost19, tổng expanded923, max_frontier6.
- IDS trên medium_maze: 69 vòng DLS, 68 lần tăng limit, cost68, tổng expanded15665, max_frontier8.

## Ghi chú
Nếu thay đổi thứ tự sinh trạng thái, số nút mở rộng và đường đi tìm được với DLS có thể thay đổi. Tính chất tối ưu của IDS trong bài này giả định chi phí bước bằng nhau.
