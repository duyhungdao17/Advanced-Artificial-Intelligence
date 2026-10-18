# Lab03 — Bài 6: Tối ưu hàm đếm xung đột bằng Numba

## Notebook
`n_queens_fast_conflict_calculation_with_numba_Bai6_Hoan_thien.ipynb` chứa đầy đủ 14 cell gốc (chỉ sửa hai nhãn trục ms -> µs cho đúng đơn vị), phần giải thích và thực nghiệm bổ sung. Notebook không cần file dữ liệu bên ngoài.

## Chạy lại
1. Cài đặt các gói: `pip install numpy matplotlib numba ipython jupyter nbclient nbconvert`.
2. Mở notebook trong VS Code/Jupyter và chọn **Restart & Run All**.
3. Các tệp kết quả mới được xuất trong thư mục tương đối `Lab03_Bai6_Results/`.

## Các bảng/ảnh
- `Bai6_Correctness_Checks.csv`: đối chiếu tính đúng đắn của ba hàm trên nhiều bàn cờ.
- `Bai6_JIT_Compile_Demo.csv`: chênh lệch minh họa giữa biên dịch JIT lần đầu và chạy nóng ở chữ ký int32 mới.
- `Bai6_Benchmark_Summary.csv`: trung vị µs/bàn cờ của 5 lần đo và hệ số tăng tốc.
- `Bai6_Benchmark_Raw.csv`: thời gian của từng lượt đo.
- `Images/Bai6_Runtime_LogLog.png`: thời gian chạy trên thang log-log.
- `Images/Bai6_Speedup_Comparison.png`: tỷ lệ tăng tốc so với naive.

## Ghi chú đo lường
- Các kết quả runtime phụ thuộc máy và tải CPU; không xem số liệu là hằng số lý thuyết.
- Benchmarks dùng 20 bàn cờ / kích thước, 5 lần đo; seed `20261016`.
- Mảng Numba đã được biên dịch trước khi đo. Lần biên dịch chữ ký `int32` là thí nghiệm riêng, không tính vào benchmark.
- Ba phương pháp bắt buộc phải trả kết quả bằng nhau ở cùng bàn cờ.
- CSV/hình nằm ở cả thư mục gốc đã đóng gói và thư mục tương đối cho phép notebook chạy lại.
