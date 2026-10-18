# LAB03 - Bài 8: Tổng hợp thí nghiệm n-Queens

## Notebook

`n_queens_Bai8_Hoan_thien.ipynb` phát triển từ bản Bài 4 đã hoàn thiện Tasks 1-5, vốn dựa trên notebook gốc của giảng viên. File người dùng gửi ở lượt này (`n_queens(1).ipynb`) là bản gốc 33 cell với Task 1-6 vẫn chưa điền. Vì vậy bản này kế thừa **bản đã hoàn thành Bài 4** để giữ đủ 5 thuật toán và hoàn thiện Task 6. Không chỉnh sửa placeholder tại phần `More Things to Do (not for credit)`.

## Chạy lại

1. Cài Python >=3.10 và gói trong `requirements.txt`.
2. Đặt notebook ở thư mục nào cũng được, mở VS Code / Jupyter và chạy `Restart & Run All`.
3. CSV và PNG của **Bài 8** được tạo trong thư mục tương đối `Lab03_Bai8_Results/`. Các CSV cũ Bài 2-4 (nếu chạy toàn bộ notebook) được ghi vào thư mục đang chạy.
4. Notebook có một cell thử mount Google Drive, nhưng khi chạy Python ngoài Colab cell này được bỏ qua. Trên Colab, cân nhắc điều chỉnh thư mục Google Drive theo nhu cầu.
5. Điền tên sinh viên và thông tin khai báo sử dụng AI ở cell đầu trước khi nộp.

## Nội dung Task 6

- Comparison: 100 trial/thuật toán cho n=4 và n=8, có 4 thuật toán trong bảng gốc và thêm Random Restart; cùng start/seed theo trial. Ghi `f` cuối, tỷ lệ thành công, số lần đánh giá và thời gian.
- Convergence: đường best-so-far n=8. Đơn vị x khác nhau giữa Hill Climbing (số move cải thiện), SA (số proposal) và RR (số lượt restart). **Không so sánh tốc độ từ trục x này.**
- Scalability: n=4,8,12,16,20, 20 trial/n/thuật toán; Steepest-ascent, First-choice, Simulated Annealing; log-log của trung vị thời gian, ước lượng độ dốc thực nghiệm (không chứng minh Big-O).
- Advanced: 100 trial/operator cho n=8 và n=12 với cùng First-choice và 5 toán tử (random-row baseline, single-step, column-swap, dual-queen, adaptive). Thời gian đến nghiệm chỉ tính các lượt thực sự đạt nghiệm.

## Các tập tin số liệu

- `Bai8_Comparison_Trials.csv`, `Bai8_Comparison_Summary.csv`
- `Bai8_Convergence.csv`
- `Bai8_Scalability_Trials.csv`, `Bai8_Scalability_Summary.csv`
- `Bai8_Move_Operators_Trials.csv`, `Bai8_Move_Operators_Summary.csv`, `Bai8_Move_Operators_Neighborhoods.csv`

Trong `Lab03_Bai8_Results/Images`: đồ thị hội tụ n=8, log-log khả năng mở rộng, tỷ lệ thành công của toán tử và hội tụ trung bình của toán tử.

## Diễn giải kết quả

- Kiểm tra tính đúng đắn bằng cách tính lại `conflicts(board)` trên tất cả nghiệm.
- Thời gian chạy có thể khác giữa các phần cứng, phiên bản Python, và độ tải hệ thống.
- Budget của các thuật toán không hoàn toàn tương đương về số lần đánh giá, cần so sánh kèm số evaluations.
- Column swap bảo toàn đa tập hàng; từ bàn cờ có hai hậu ở cùng hàng không thể đạt nghiệm hoàn chỉnh chỉ với toán tử này.
- Các thuật toán mang tính ngẫu nhiên có kết quả thành công tái lập theo seed; phép đo thời gian chỉ mang tính tham khảo.
