# Lab03 – Bài 3: Steepest-ascent và Stochastic Hill Climbing (n-Queens)

## Nội dung
- `n_queens_Bai3_Hoan_thien.ipynb`: giữ nguyên phần Bài 2 và các hướng dẫn Task, điền code Task 1–3; Task 4–6 được giữ lại để thực hiện sau.
- `n_queens_Bai3_Hoan_thien.html`: bản có kết quả đã chạy (nếu có).
- `Bai3_Demo_Results.csv`: kết quả 4-Queens và 8-Queens với cùng bàn cờ ban đầu.
- `Bai3_Trial_Results.csv`: 20 bàn cờ khởi tạo cho mỗi n, chạy cùng 3 thuật toán.
- `Bai3_Summary_Results.csv`: thống kê trung bình, tỉ lệ thành công.
- `Images/Bai3_HillClimbing_Comparison.png`: đồ thị hội tụ và số lần đánh giá hàm mục tiêu.

## Chạy lại
Cần Python và các thư viện: numpy, matplotlib, pandas, notebook/ipykernel.
Mở notebook và chọn Restart & Run All; không cần file hỗ trợ bên ngoài. Seed được đặt rõ trong phần thực nghiệm. Các file CSV và PNG sẽ được xuất với đường dẫn tương đối trong thư mục notebook. Không chạy qua đường dẫn tuyệt đối.

## Quy ước đo
- `steps`: số bước chuyển trạng thái được chấp nhận.
- `evaluations`: số lần `conflicts()` được gọi **bên trong hàm tìm kiếm**, gồm trạng thái đầu (không tính các lệnh kiểm tra/thể hiện kết quả phía ngoài hàm).
- `elapsed_ms`: thời gian thực thi một lần thuật toán, không tính vẽ biểu đồ bên ngoài.
- `TRY_LIMIT` của first-choice là giới hạn lấy mẫu; không đồng nghĩa chắc chắn hết mọi hướng cải thiện.
- Đồ thị thời gian trung bình có thể nhiễu; hãy đo nhiều lần nếu cần độ tin cậy cao hơn.

Phần cài đặt này phục vụ thực hành và tham khảo; người học cần hiểu và kiểm tra mã trước khi nộp theo chính sách môn học.
