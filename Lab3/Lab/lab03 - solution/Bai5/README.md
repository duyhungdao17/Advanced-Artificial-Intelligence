# LAB03 — Bài 5: Khảo sát lịch giảm nhiệt độ

## Nội dung
- `Simulated_Annealing_Schedules_Bai5_Hoan_thien.ipynb`: notebook giữ nguyên 14 cell gốc của Michael Hahsler, bổ sung 16 cell Code/Markdown để thực hiện bài tập.
- `Simulated_Annealing_Schedules_Bai5_Hoan_thien.html`: báo cáo HTML đã chạy, có đồ thị.
- `Images/`: 5 hình: bốn lịch nhiệt, độ nhạy tham số, xác suất chấp nhận bước xấu, tỷ lệ thành công n-Queens và hội tụ n-Queens.
- `Bai5_Temperature_Values.csv`: bảng nhiệt độ tại các vòng lặp khảo sát.
- `Bai5_SA_Trials.csv`: chi tiết 160 lượt SA (4 lịch x 2 kích thước x 20 trial).
- `Bai5_SA_Summary.csv`: tỷ lệ thành công, f tốt nhất trung bình, số lần thử, số lần chấp nhận bước xấu, thời gian.
- `Bai5_Parameter_Trials.csv`, `Bai5_Parameter_Summary.csv`: độ nhạy với alpha, eta, T0 (64 lượt trên n=8).

## Hướng dẫn chạy
1. Giải nén vào một thư mục. Mở `.ipynb` trong JupyterLab/VS Code/Colab.
2. Cài đặt nếu thiếu: `pip install numpy matplotlib pandas nbformat nbclient ipykernel`.
3. Chọn **Restart & Run All** từ trên xuống. Chương trình dùng đường dẫn tương đối `Images/` và CSV ngay trong thư mục chạy notebook.
4. Đặt working directory về thư mục chứa notebook nếu IDE chưa tự đặt.

## Cấu hình và lưu ý
- Seed gốc: `20261015`.
- Các lịch sử dụng t=1,2,... để đảm bảo logarithmic xác định; T(1)=T0/ln2 với lịch Logarithmic.
- Hình so sánh công thức: T0=3, alpha=0.97, eta=0.025, t=1..120.
- Benchmark n-Queens: T0=3, alpha=0.995, eta=0.002, max_iter=1500, n=4/8, 20 trial mỗi cấu hình. Cùng một seed và bàn cờ khởi đầu giữa các lịch trong mỗi trial.
- `temperature_linear()` gốc có thể trả về T âm: trong hàm SA, chặn `max(0,T)`; nếu T=0 thì không chấp nhận bước xấu.
- SA sử dụng cấu trúc trạng thái và hàm đếm xung đột tương đương Task 5 Bài 4, nhưng độc lập với notebook Bài 4; chạy lại chỉ cần file này.
- `elapsed_ms` chỉ là thời gian thực nghiệm, phụ thuộc phần cứng và tải của môi trường.

## Kết quả mẫu (20 lần chạy)
| n | Exponential | Linear | Fast | Logarithmic |
|---|---:|---:|---:|---:|
|4|100%|100%|100%|100%|
|8|75%|55%|90%|85%|

Đây là tỷ lệ quan sát, không phải chứng minh lịch Fast tối ưu nói chung.
