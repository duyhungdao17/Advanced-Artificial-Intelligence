# Lab03 – Bài 2: Mô hình hóa bài toán n-Queens

## Các tệp

- `n_queens_Bai2_Hoan_thien.ipynb`: notebook gốc được giữ nguyên và bổ sung 10 cell Code/Markdown **trước phần # Tasks** để hoàn thành Bài 2 (n-Queens modelling).
- `Bai2_nQueens_Results.csv`: bảng kết quả thực nghiệm 4-Queens, 8-Queens và cấu hình chuẩn `[1,3,0,2]`.
- `Images/*.png`: ảnh do các cell thực thi trong notebook tạo ra.
- `n_queens_Bai2_Hoan_thien.html`: bản xem nhanh với các hình và output (nếu có).

## Cách chạy

1. Mở file `.ipynb` bằng VS Code/Jupyter.
2. Chọn Python kernel đã cài `numpy`, `matplotlib`, `ipython` và chạy `Restart & Run All`.
3. Notebook gốc có cell Google Colab mount Drive tùy chọn. Khi chạy trên Jupyter/VS Code ngoài Colab, cell tự bỏ qua phần mount.
4. Các cell Bài 2 sử dụng seed `20261015` để kết quả bàn cờ ngẫu nhiên có thể tái lập.

## Kết quả đã kiểm chứng

- 4-Queens ngẫu nhiên `[3,0,3,1]`: `conflicts=1`, 12 láng giềng, có 1 láng giềng đạt `conflicts=0`.
- 4-Queens mẫu `[1,3,0,2]`: `conflicts=0`, 12 láng giềng.
- 8-Queens ngẫu nhiên `[6,3,2,3,1,0,5,2]`: `conflicts=7`, 56 láng giềng, 17 bước cải thiện.
- Bài 2 là mô hình hóa, chưa triển khai thuật toán tối ưu; các ô **Task 1–6** của notebook gốc được giữ lại cho Bài 3, 4 và 8.

## Giải thích hàm conflicts()

`conflicts(board)` đếm **cặp hậu** tấn công nhau, qua số quân cùng hàng và hai loại đường chéo bằng tổ hợp `k(k−1)/2`. Vì biểu diễn một hậu mỗi cột, không cần xét trùng cột.

## Lưu ý

Hãy cập nhật mục `Student Name` và khai báo AI tools/đóng góp học thuật trong cell đầu notebook trước khi nộp. Không tự nhận đã hoàn thành Task 1–6 chỉ vì notebook chạy được (các ô TODO vẫn còn theo đúng phạm vi Bài 2).
