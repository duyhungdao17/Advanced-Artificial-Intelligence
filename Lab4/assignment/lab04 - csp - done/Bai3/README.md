# LAB04 – Bài 3: Backtracking Search, MRV và LCV

## Nguồn và phạm vi
- Tiếp nối notebook Bài 2 của Lab04; giữ nguyên 37 cell đã có và thêm 11 cell cho Bài 3.
- Dữ liệu: đồ thị Delaunay n=10, seed=1111, 21 cạnh; palette 4 hoặc 3 màu.
- Bài 4 (Forward Checking, Min-Conflicts) vẫn là TODO, chưa triển khai.

## Chạy lại
1. Cài thư viện bằng `pip install -r requirements.txt`.
2. Mở `CSP_graph_coloring_example_Bai3_Hoan_thien.ipynb` ở Jupyter/VS Code.
3. Chọn Restart & Run All, chạy từ gốc; kết quả CSV/PNG xuất vào Lab04_Bai1_Results, Lab04_Bai2_Results, Lab04_Bai3_Results bằng đường dẫn tương đối.
4. Có bản HTML xuất từ notebook đã chạy để xem nhanh.

## Thuật toán
- Baseline: hàm `backtrack_search()` gốc của giảng viên, first-unassigned, original-domain.
- MRV: số màu hợp lệ còn lại ít nhất; hòa theo thứ tự biến gốc.
- MRV + LCV: thứ tự biến MRV; với giá trị của biến, chỉ xét màu khả dụng theo các đỉnh đã gán, chọn màu làm hạn chế ít màu hợp lệ ở đỉnh kề chưa gán nhất. LCV cũng có bước bỏ màu chắc chắn không hợp lệ, vì vậy số attempts khác MRV do cả lọc màu và thứ tự.
- COUNT là số lần hàm đệ quy được gọi, tính cả nút gốc. `attempts` là số phép gán thử, kể cả thất bại; không đồng nhất.
- Đồ thị chứa K4 trên các đỉnh (2,3,4,9), nên 3 màu vô nghiệm (được kiểm chứng bằng cả lý thuyết và backtracking vét cạn).

## Benchmark
- Trên mỗi CSP và chiến lược, 20 lần chạy; báo cáo trung vị, trung bình thời gian (ms), COUNT, số lần thử gán, số lần quay lui và độ sâu lớn nhất.
- Dùng cùng mô hình và cùng đồ thị; chỉ so sánh độ ưu tiên biến/màu và chi phí tính heuristic.
- Thời gian phụ thuộc môi trường máy, kết quả không có tính bảo đảm phổ quát.

## Kết quả
- `Lab04_Bai3_Results/Bai3_Backtracking_Comparison.csv` — thống kê 3 chiến lược x 2 miền.
- `Lab04_Bai3_Results/Bai3_Backtracking_Timing_Raw.csv` — 120 lần đo thời gian.
- `Lab04_Bai3_Results/Bai3_Backtracking_COUNT_Attempts.png` — bảng trực quan công sức.
- `Lab04_Bai3_Results/Bai3_Graph_Coloring_Strategies.png` — nghiệm 4 màu trên cùng đồ thị.
- Các kết quả từ Bài 1 và Bài 2 nằm trong thư mục kết quả tương ứng.
