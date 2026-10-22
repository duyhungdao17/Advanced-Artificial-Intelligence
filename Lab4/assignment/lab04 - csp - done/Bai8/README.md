# LAB04 — Bài 8: Đánh giá tổng hợp và bài nâng cao

Notebook chính: `n_queens_Bai8_Hoan_thien.ipynb` (kế thừa Bài 5, 6, 7, hoàn thành Task 6 và Advanced Task).

## Thực hiện
1. Cài thư viện theo `requirements.txt` (`pip install -r requirements.txt`).
2. Mở notebook trong JupyterLab/VS Code và chọn **Restart & Run All**.
3. Không cần đường dẫn tuyệt đối; thư mục `Lab04_Bai5_Results`, `Lab04_Bai6_Results`, `Lab04_Bai7_Results`, `Lab04_Bai8_Results` sẽ xuất từ các cell.
4. Mở `n_queens_Bai8_Hoan_thien.html` để xem bản đã chạy. CSV và PNG từ lần chạy minh họa được lưu sẵn.

## Thiết lập
- Seed chính Bài 8: `20261020`.
- Task 6: 100 board **phân biệt** tại mỗi n = 4, 8; 8 cấu hình thuật toán; 1.600 lượt. Ngân sách HC tối đa 1.000 bước, RR tối đa 100 lần khởi động lại (101 lượt kể cả lượt đầu), SA tối đa 2.000 lần thử; hai lịch Exponential (T0=3, alpha=0.995) và Linear (T0=3, eta=0.002).
- Hội tụ: cùng bàn cờ n=8, trục x theo đơn vị khác nhau; **không** so sánh tốc độ bằng vị trí trực tiếp của các điểm trên đồ thị.
- Khả năng mở rộng: n = 4, 8, 12, 16, 20; 25 lượt mỗi cấu hình; Steepest, First-choice, SA Exponential (**500** lượt thử theo ngân sách riêng); 375 lượt.
- Advanced Task: n = 8, 12, 100 board **phân biệt**/kích thước, 5 toán tử, 1.000 lượt; tối đa 400/700 thử và 120/250 thất bại liên tiếp.
- Thời gian ở các bảng tính bằng mili giây (ms), có thể khác nhau trên máy khác.

## Thư mục Bài 8
- `Bai8_Task6_Trials.csv`, `Bai8_Task6_Summary.csv`.
- `Bai8_Convergence_Representative_n8.csv`, `Bai8_Convergence_n8.png`.
- `Bai8_Scalability_Trials.csv`, `Bai8_Scalability_Summary.csv`, `Bai8_Scalability_LogLog.png`.
- `Bai8_Advanced_Trials.csv`, `Bai8_Advanced_Summary.csv`, `Bai8_Advanced_Neighborhoods.csv`, `Bai8_Advanced_Convergence_Raw.csv` và ba hình minh họa Advanced.
- Các file `Bai8_Task6_Success_Rates.png`, `Bai8_Task6_Evaluations.png`.

## Lưu ý diễn giải
- `solved` chỉ đúng khi h = 0; `final_h` đối với RR và SA là **nghiệm tốt nhất từng gặp**.
- Các ngân sách giữa HC/RR/SA khác nhau; không kết luận thuật toán luôn tốt hơn dựa chỉ vào success rate.
- `column-swap` không thay đổi multiset hàng; nếu board có hậu trùng hàng thì chỉ swap không thể trở thành nghiệm.
- Hệ số dốc trên đồ thị log-log phản ánh số đo với ngân sách và phần cứng đã dùng, **không phải chứng minh Big-O**.
- `mean_success_ms` ở những toán tử không có lượt giải thành công là NaN (không có số liệu).

## Số liệu chính n=8 (Task 6, 100 lượt)

| algorithm        |   success_percent |   mean_final_h |   mean_evaluations |   mean_ms |
|:-----------------|------------------:|---------------:|-------------------:|----------:|
| First-choice     |                11 |           1.32 |             212.23 |      2.78 |
| RR-First-choice  |               100 |           0    |            1904.01 |     25.78 |
| RR-Steepest      |               100 |           0    |            1840.43 |     16.32 |
| RR-Stochastic    |               100 |           0    |            2237.35 |     21.95 |
| SA-Exponential   |                91 |           0.09 |             890.71 |     13.03 |
| SA-Linear        |                70 |           0.3  |            1606.21 |     22.35 |
| Steepest-ascent  |                12 |           1.31 |             230.04 |      1.92 |
| Stochastic (all) |                11 |           1.31 |             334.2  |      3    |

Kiểm tra: 27 cell Code; 68 cell tổng, không có outputs lỗi trong notebook đã chạy.
