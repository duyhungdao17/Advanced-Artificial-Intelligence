# LAB04 CSP — Bài 6: Các biến thể Hill Climbing (n-Queens)

## Nội dung
Notebook `n_queens_Bai6_Hoan_thien.ipynb` kế thừa trực tiếp Bài 5 và hoàn thiện:

- Task 1: `steepest_ascent` — duyệt toàn bộ lân cận, chọn tốt nhất.
- Task 2: `inefficient_stochastic` — duyệt toàn bộ lân cận, chọn ngẫu nhiên trong tập cải thiện.
- Task 3: `efficient_stochastic` — thử từng lân cận ngẫu nhiên có hoàn lại, chấp nhận bước cải thiện đầu; có ngưỡng số lần thử thất bại liên tiếp.
- Các ca kiểm thử, bảng kết quả của lượt demo trên n=4/8 và khảo sát bổ sung 30 lượt/kích thước/thuật toán (180 lượt tổng cộng), biểu đồ hội tụ, số lần đánh giá và tỷ lệ thành công.

Các ô Task 4, Task 5, Task 6, Advanced Task gốc vẫn để trống, sẽ hoàn thiện trong Bài 7–8. Thống kê 100 lượt trong Task 6 **chưa** được thực hiện ở Bài 6.

## Chạy lại
1. Mở terminal tại thư mục chứa notebook.
2. Cài `pip install -r requirements.txt` nếu cần.
3. Mở notebook trong Jupyter hoặc VS Code, chọn `Restart & Run All`.
4. Notebook tạo tự động `Lab04_Bai5_Results/` và `Lab04_Bai6_Results/` bằng đường dẫn tương đối. Không dùng đường dẫn cá nhân.

## Bảng kết quả Bài 6
- `Bai6_HillClimbing_Demo.csv`: 6 lượt minh họa cùng board Bài 5 (n=4,8).
- `Bai6_HillClimbing_Trials.csv`: 180 lượt độc lập có seed.
- `Bai6_HillClimbing_Summary.csv`: thống kê theo thuật toán/kích thước.
- `Bai6_HillClimbing_Validation.csv`: trạng thái dừng và kiểm thử.

## Chỉ số
- `final_h`: số cặp hậu xung đột khi kết thúc.
- `steps`: số bước *được chấp nhận*, chỉ gồm nước đi h giảm.
- `evaluations`: số lượt gọi `conflicts()` **trong thuật toán**, bao gồm lần đánh giá ban đầu.
- `status=LOCAL_MINIMUM`: không còn nước đi cải thiện sau khi xét toàn bộ lân cận.
- `status=TRY_LIMIT`: First-choice đã hết ngưỡng lấy mẫu, **không chứng minh** là cực tiểu cục bộ.
- `elapsed_ms`: thời gian một lượt gọi thuật toán trên máy thực thi; chỉ là số đo tham khảo, có biến động theo môi trường.

Cấu hình seed Bài 5 = 20261020; ngưỡng `max_no_improvement` mặc định để xác suất bỏ sót một nước đi cải thiện xác định không quá 5% trong giả định lấy mẫu có hoàn lại. Bộ kiểm tra nội dung gốc và các giá trị `conflicts()` của Bài 5 được giữ nguyên.

## Xuất HTML
`jupyter nbconvert --to html n_queens_Bai6_Hoan_thien.ipynb`

## Học thuật
Nội dung bổ sung được hỗ trợ bởi ChatGPT. Sinh viên cần đọc hiểu và tự kiểm tra trước khi nộp; xem phần khai báo ở đầu notebook.
