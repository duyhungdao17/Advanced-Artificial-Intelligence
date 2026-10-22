# LAB04 – Bài 7: Random Restart và Simulated Annealing (n-Queens)

## Nội dung
- Kế thừa toàn bộ Bài 5–6, giữ các hàm gốc `random_board`, `conflicts`, `show_board` và Task 1–3.
- Hoàn thiện Task 4: `random_restart_hill_climbing`, ba biến thể Steepest-ascent, Inefficient Stochastic, Efficient Stochastic.
- Hoàn thiện Task 5: `simulated_annealing_queens`, lịch Exponential và Linear, chấp nhận các bước xấu theo xác suất `exp(-Δh/T)`.
- Chưa điền Task 6 và Advanced Task, để làm trong Bài 8.

## Chạy lại
1. Cài thư viện trong requirements.txt bằng `pip install -r requirements.txt`.
2. Mở `n_queens_Bai7_Hoan_thien.ipynb` với Jupyter hoặc VS Code.
3. Chọn **Restart & Run All** và chạy từ thư mục chứa notebook.
4. Notebook tự xuất ba thư mục `Lab04_Bai5_Results/`, `Lab04_Bai6_Results/`, `Lab04_Bai7_Results/` bằng đường dẫn tương đối.
5. File HTML là bản xem nhanh của notebook đã chạy.

## Thiết lập Bài 7
- Random seed Bài 7: `20261020`. Bài 5/6 giữ seed như bản đã nộp.
- Task 4: `max_restarts=100` = tối đa 100 lần khởi động lại **sau lượt đầu**; tức tối đa 101 lượt HC. Dừng sớm khi `h=0`; trả nghiệm tốt nhất nếu hết ngân sách.
- Task 5: T0=3, alpha=0.995, eta=0.002, tối đa 2000 lần thử một lượt. Linear chặn nhiệt độ tại 0; khi T=0 chỉ nhận Δh <= 0.
- Khảo sát minh họa: 30 bàn cờ khác nhau cho mỗi n=4/8 và mỗi phương pháp (5 cấu hình × 2 n × 30 = 300 lượt). Task 6 (Bài 8) yêu cầu >=100 lượt/thiết lập, chưa thực hiện ở đây.
- `evaluations`: số lần gọi `conflicts()` **trong mỗi thuật toán**, gồm lần đánh giá ban đầu; không tính các lần kiểm tra bên ngoài. Với RR, cộng tất cả lượt HC.
- `steps`: RR là tổng bước cải thiện của Hill Climbing; SA là tổng bước chấp nhận, gồm bước xấu. Không so sánh trực tiếp hai đại lượng mà không chuẩn hóa.
- Hai phương pháp có ngân sách khác nhau; khi diễn giải so sánh phải xét tỷ lệ thành công cùng số lần đánh giá và thời gian.

## CSV của Bài 7
- `Bai7_Demo_Results.csv` — kết quả trên cùng bàn cờ từ Bài 5.
- `Bai7_Trial_Results.csv` — dữ liệu 300 lượt chạy.
- `Bai7_Summary_Results.csv` — tổng hợp theo kích thước và thuật toán.
- `Bai7_Validation.csv` — kiểm thử.
- `Bai7_Restart_Trace.csv` — lịch sử từng lượt restart trong demo.
- `Bai7_SA_Convergence.csv` — lịch sử nhiệt độ, h hiện tại và h tốt nhất trong demo.

## PNG của Bài 7
- `Bai7_Cooling_Schedules.png` — đồ thị nhiệt độ và p chấp nhận Δh=+1.
- `Bai7_SA_Convergence.png` — đồ thị hội tụ SA trên n=8.
- `Bai7_Success_and_Evaluations.png` — so sánh tỷ lệ thành công và số lần đánh giá.

**Lưu ý:** Không coi `ITERATION_LIMIT` / `RESTART_LIMIT` là chứng minh vô nghiệm. Trong SA, nghiệm tốt nhất có thể khác trạng thái cuối.
