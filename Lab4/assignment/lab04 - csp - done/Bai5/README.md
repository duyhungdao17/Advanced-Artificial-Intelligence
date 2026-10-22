# LAB04 – Bài 5. Biểu diễn bài toán n quân hậu

## Tệp chính

- `n_queens_Bai5_Hoan_thien.ipynb`: notebook **gốc** của giảng viên, được thêm mã và giải thích tiếng Việt cho Bài 5 trước mục `# Tasks`.
- `n_queens_Bai5_Hoan_thien.html`: bản xuất HTML đã thực thi, bao gồm hình/đầu ra ngay trong HTML.
- `Lab04_Bai5_Results/`: bảng kết quả và hình PNG được tự tạo bằng notebook.

## Yêu cầu của Bài 5 đã làm

1. Khảo sát `random_board()`, `show_board()`, `conflicts()`; giải thích vector `board` một quân hậu/cột.
2. Vẽ 4-Queens và 8-Queens ngẫu nhiên; so sánh mẫu 4-Queens `[1,3,0,2]` và cấu hình 8-Queens tham chiếu.
3. Định nghĩa h(board) = số cặp hậu cùng hàng/đường chéo; kiểm tra h=0 tương đương không có cặp hậu tấn công nhau.
4. Kiểm thử `conflicts()` với kiểm tra độc lập từng cặp: toàn bộ 256 trạng thái n=4 và 500 mẫu n=8.

## Tái lập thực nghiệm

1. Cài đặt các thư viện: `pip install -r requirements.txt`.
2. Mở notebook và chọn **Restart & Run All**.
3. Code Bài 5 dùng `np.random.seed(20261020)`; cell ví dụ sẵn có phía trên vẫn dùng seed `1234` của notebook gốc, vì vậy hai cấu hình 4-Queens hiển thị ở hai phần có thể khác nhau.
4. Kết quả được ghi vào thư mục tương đối `Lab04_Bai5_Results/` tạo ngay nơi notebook chạy.
5. Nếu chạy trên Google Colab và muốn lưu vào Drive, hãy mount Drive theo nhu cầu. Ô thiết lập gốc đã bỏ lệnh đổi tự động sang đường dẫn Drive cá nhân để tránh lỗi đường dẫn.

## Bảng và hình

- `Bai5_Queens_Boards.csv`: các vector thử nghiệm, số xung đột, tính hợp lệ, kích thước không gian trạng thái.
- `Bai5_Queens_Validation.csv`: số lượng test và kết quả đối chiếu từng cặp.
- `Bai5_Queens_Conflict_Pairs.csv`: các cặp cột có quân hậu xung đột.
- `Bai5_4Queens_Random.png`, `Bai5_4Queens_Reference.png`, `Bai5_8Queens_Random.png`, `Bai5_8Queens_Reference.png`.

## Phạm vi

Các ô `# Code and description go here` trong Task 1–6 và Advanced task **chưa được điền**. Đây là các nội dung Bài 6–8, giữ nguyên để tiếp tục thực hiện trong các bài sau. Người học cần tự xác nhận phần tuyên bố về tính độc lập bài làm trên đầu notebook trước khi nộp.
