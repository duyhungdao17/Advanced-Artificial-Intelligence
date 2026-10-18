# Lab03 – Bài 4: Random Restart và Simulated Annealing (n-Queens)

## Nội dung bộ file

- `n_queens_Bai4_Hoan_thien.ipynb`: giữ bài 2–3, điền đúng Task 4–5, thực nghiệm, đồ thị, nhận xét; Task 6 để nguyên cho Bài 8.
- `n_queens_Bai4_Hoan_thien.html`: bản xem nhanh có kết quả đã chạy.
- `Bai4_Demo_Results.csv`: kết quả các thuật toán trên trạng thái mẫu từ Bài 2.
- `Bai4_Trial_Results.csv`, `Bai4_Summary_Results.csv`: số liệu và tổng hợp 20 trial / n = 4, 8.
- `Bai4_SA_Temperature_Trials.csv`, `Bai4_SA_Temperature_Summary.csv`: kết quả thay đổi T0 và alpha.
- `Images/Bai4_SA_Convergence.png`: hàm mục tiêu hiện tại và tốt nhất trong SA.
- `Images/Bai4_RR_SA_Success_Rates.png`: tỷ lệ đạt f=0 cho hai kích thước bàn cờ.

## Cách chạy

Cần Python, Jupyter Notebook / VS Code, numpy, matplotlib, pandas, IPython.
Đặt notebook tại thư mục có quyền ghi và chạy `Restart & Run All` từ trên xuống. Không cần file phụ trợ.
CSV và hai ảnh PNG sẽ được xuất trong thư mục đang chạy notebook bằng đường dẫn tương đối.
Notebook giữ nguyên khối Colab `try/except ImportError` của giảng viên; khi chạy trên máy thông thường khối này bị bỏ qua.

## Quy ước

- Random Restart: `max_starts=100` nghĩa là **tối đa 100 lượt chạy kể cả lượt đầu**, nên `restarts_used = runs - 1` (≤99).
- Kết quả Random Restart là bàn cờ có `best_f` nhỏ nhất; dừng sớm ngay khi `best_f = 0`.
- SA sinh tối đa 2500 láng giềng, nhiệt độ `T(t)=T0*alpha**t`; ở `delta=0` chấp nhận trạng thái mới, ở `delta>0` chấp nhận với xác suất `exp(-delta/T)`.
- SA theo dõi cả `final_current_f` và `best_f`; hàm mục tiêu hiện tại có thể tăng. `board` trả về nghiệm tốt nhất đã gặp, `final_board` là trạng thái ở thời điểm kết thúc.
- `evaluations`: số lần gọi hàm `conflicts()` bên trong thuật toán, bao gồm trạng thái đầu của từng lần khởi tạo. `elapsed_ms`: thời gian một lần thực thi; không bao gồm việc vẽ hình và không nhất thiết tái lập ở các máy khác.
- `SOLVED` khi `best_f=0`; `RESTART_LIMIT` hoặc `ITERATION_LIMIT` có nghĩa hết ngân sách, **không phải** không có lời giải.
- 20 lần chạy cho mỗi cỡ bàn cờ là thí nghiệm Bài 4; Task 6 (Bài 8) cần chạy ít nhất 100 lần theo hướng dẫn notebook gốc.
- RR và SA sử dụng ngân sách tính toán khác nhau (lượt khởi tạo vs lượt đánh giá láng giềng), vì thế không nên kết luận ưu thế chỉ từ tỷ lệ thành công.

Nội dung này là bản cài đặt thực hành bổ sung và cần được người học xem lại trước khi nộp.
