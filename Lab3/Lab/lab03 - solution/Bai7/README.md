# LAB03 — Bài 7: Traveling Salesman Problem (TSP)

## Tài liệu
- `traveling_salesman_problem_Bai7_Hoan_thien.ipynb`: notebook chính, đã điền các ô thuật toán và chạy kiểm thử.
- `traveling_salesman_problem_Bai7_Hoan_thien.html`: bản HTML chứa mã và các kết quả đã thực thi.
- `Lab03_Bai7_Results/*.csv`: bảng minh họa, bảng 125 lượt chạy và bảng thống kê.
- `Lab03_Bai7_Results/*.png`: tour trước/sau tối ưu, hội tụ, chất lượng, thời gian theo số thành phố.

## Hướng dẫn chạy
1. Cài đặt Python và Jupyter/JupyterLab hoặc dùng VS Code với Python kernel.
2. Cài các thư viện: `pip install numpy pandas scipy matplotlib nbformat nbclient ipykernel` (nbformat/nbclient tùy chọn, cần cho kiểm thử tự động; notebook chỉ cần 4 thư viện đầu).
3. Mở notebook, thực hiện **Restart & Run All**.
4. File kết quả tự xuất vào thư mục `Lab03_Bai7_Results/` bằng đường dẫn tương đối.

## Mô hình
- Các thành phố có tọa độ 2D ngẫu nhiên trong hình vuông đơn vị; khoảng cách Euclidean đối xứng.
- Tour là hoán vị các chỉ số thành phố, phải quay lại thành phố xuất phát.
- Hàm mục tiêu: `tour_length(tsp, tour)`; nhỏ hơn là tốt hơn.
- Toán tử lân cận thống nhất: **swap** hai thành phố ở vị trí i, j (i < j). Mỗi tour n thành phố có `n*(n-1)//2` lân cận.
- Không khẳng định đã tìm được tối ưu toàn cục. Các heuristic tìm cực tiểu cục bộ hay nghiệm tốt nhất trong ngân sách.

## Thuật toán chính
- **Steepest-ascent**: lựa chọn giảm độ dài tour nhiều nhất trong toàn bộ lân cận; mặc dù tên gọi “ascent” trong tài liệu, bài này là tối thiểu hóa.
- **Random Restarts**: tối đa 8 lượt khởi tạo, dùng Steepest-ascent; tính cả lượt ban đầu, tức tối đa 7 lần khởi động lại.
- **Stochastic (all)**: đánh giá toàn bộ swap, chọn ngẫu nhiên trong số các swap giảm chi phí.
- **First-choice**: sinh lân cận ngẫu nhiên đến khi có cải thiện; dừng theo giới hạn số thử thất bại/liên tiếp, không chứng minh local optimum.
- **Simulated Annealing**: dùng `T(t) = 0.20*0.995**t`, tối đa 1500 lần thử, bước xấu hơn được chấp nhận theo `exp(-delta/T)`; lưu nghiệm tốt nhất từng tìm thấy.
- Genetic Algorithm là **bonus**, để nguyên là chưa triển khai.

## Thiết lập benchmark
- Số thành phố: `6, 10, 15, 20, 25`.
- 5 trial mỗi kích thước, 5 thuật toán, tổng cộng 125 lượt.
- Cùng `tsp_i`, `init_i` cho cả năm thuật toán ở từng (n, trial).
- Seed: `20261015 + 100*n + trial` (trial bắt đầu từ 0).
- Lưu chi phí tour, phần trăm cải thiện, số bước chấp nhận, số lần đánh giá, thời gian `perf_counter` tính bằng ms.
- Random Restarts thực hiện nhiều lượt tìm kiếm hơn; các phương pháp có ngân sách khác nhau, **không so sánh như cùng số lần đánh giá**.
- Thời gian đo có thể thay đổi tùy máy và tải hệ thống; các giá trị CSV là kết quả của lượt thực thi đã ghi.

## Ghi chú thay đổi so với notebook gốc
- Giữ các helper gốc: `random_tour`, `random_tsp`, `tour_length`, `show_tsp`.
- Thêm `random.seed(1234)` để hàm `random_tour()` có thể lặp lại kết quả, bên cạnh `np.random.seed(1234)` của notebook gốc.
- Sửa hai lỗi hiển thị nhỏ: dòng hướng dẫn Steepest-ascent sao chép từ n-Queens và dấu ngoặc thừa của dòng in ma trận khoảng cách.
- Thay ô thời gian mẫu `Do something` bằng ghi chú dùng `perf_counter()` thật.
- Đã kiểm chứng các tour là hoán vị hợp lệ, kết quả chi phí khớp hàm `tour_length()` và notebook chạy không lỗi.
