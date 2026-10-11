# Lab 02 — Bài 6: Ảnh hưởng của heuristic

## Thành phần
- `06_Explore_heuristics_Bai6_Hoan_thien.ipynb`: notebook của giảng viên (24 cell) + 18 cell Code/Markdown bổ sung Bài 6; đã chạy thành công 20 cell Code.
- `small_maze.txt`: dữ liệu thực nghiệm bổ sung có tường, từ Bài 2 (tùy chọn).
- `ket_qua_bai6_me_cung_rong.csv`: bảng so sánh BFS, GBFS, A* trong lưới rỗng 10×10.
- `ket_qua_bai6_small_maze.csv`: bảng so sánh trên `small_maze.txt`.
- `hinh_bai6_heatmaps.png`: 6 bản đồ h(n)/f(n) cho Manhattan, Euclidean, Chebyshev.
- `hinh_bai6_hieu_suat_me_cung_rong.png`: biểu đồ hiệu suất.
- `hinh_bai6_duong_di_small.png`: ví dụ đường đi BFS, GBFS-Manhattan, A*-Manhattan.

## Cách chạy
1. Giải nén tất cả file vào một thư mục.
2. Cài Python và các package: `python -m pip install notebook numpy matplotlib pandas ipykernel` (hoặc mở trong Google Colab).
3. Mở `06_Explore_heuristics_Bai6_Hoan_thien.ipynb` rồi chạy **Restart & Run All**.
4. Notebook không phụ thuộc `maze_helper.py` hoặc `tree_search_solution.py`.
5. Khi thiếu `small_maze.txt`, cell khảo sát bản đồ có tường sẽ tự bỏ qua; các phần còn lại vẫn chạy.

## Phương pháp so sánh
- Mê cung rỗng 10×10: S=(1,1), G=(8,8) (đánh số từ 0), di chuyển 4 hướng với cost=1.
- GBFS ưu tiên theo h. A* ưu tiên f=g+h, khi hòa f ưu tiên h thấp hơn, sau đó theo thứ tự chèn.
- `Nodes expanded`: số trạng thái lấy ra khỏi frontier và sinh láng giềng, loại trừ goal.
- `Max frontier`: số vị trí đang chờ xét, bỏ qua bản ghi heap lỗi thời.
- Các con số không so sánh được trực tiếp với notebook Bài 5 nếu quy ước tie-break khác nhau.
- Thời gian thực thi không thể kết luận chắc chắn từ một lần chạy trên lưới rất nhỏ. Dùng số nút mở rộng/độ dài đường đi làm đại lượng chính.

## Nội dung lý thuyết quan trọng
- Manhattan là perfect heuristic trong lưới rỗng 4 hướng (cost mỗi bước = 1).
- Euclidean và Chebyshev admissible, consistent nhưng thường kém thông tin hơn Manhattan với bài toán 4 hướng.
- A* tối ưu với cách quản lý trạng thái đúng và heuristic consistent; có thể cần mở lại trạng thái nếu heuristic chỉ admissible nhưng không consistent.
- GBFS không bảo đảm đường đi tối ưu trên mê cung có tường.
