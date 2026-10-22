# LAB04 – Bài 1: Biểu diễn CSP và sinh đồ thị cần tô màu

## Cấu trúc

- `CSP_graph_coloring_example_Bai1_Hoan_thien.ipynb`: Notebook gốc của giảng viên, được bổ sung 11 cell Markdown/Code cho Bài 1; 18 cell gốc vẫn giữ nguyên nguồn mã để làm tiếp Bài 2–4.
- `Lab04_Bai1_Results/`: 3 bảng CSV và 2 ảnh minh họa được xuất bằng đường dẫn tương đối khi chạy lại notebook.
- `requirements.txt`: các gói Python tối thiểu phục vụ chạy notebook.

## Cách chạy

1. Giải nén và mở notebook bằng Jupyter Notebook/JupyterLab hoặc VS Code; thư mục làm việc là thư mục chứa notebook.
2. Cài các thư viện còn thiếu: `python -m pip install -r requirements.txt`.
3. Chạy `Restart & Run All` từ trên xuống. Các file ở `Lab04_Bai1_Results/` sẽ được tạo lại.
4. Giữ nguyên seed `1111` và `n=10` của notebook gốc để kết quả trùng minh họa.

## Phát hiện chính

- 10 biến/đỉnh, 21 cạnh không hướng; tổng bậc = 42.
- Mỗi ràng buộc cho cạnh `(i,j)` với `i<j` biểu diễn hai đầu cạnh khác màu, tránh ghi trùng cạnh.
- Miền 4 màu có nghiệm đầy đủ, hợp lệ (Backtracking cơ bản kiểm chứng).
- Miền 3 màu không có nghiệm ở **đồ thị cụ thể này**, vì có K4 gồm các đỉnh (2,3,4,9).
- `complete` không đồng nghĩa `consistent`: mọi đỉnh màu đỏ là phép gán đầy đủ nhưng sai ở cả 21 cạnh.

## Phạm vi

Notebook có chạy các ví dụ `complete`, `consistent` và `backtrack_search` vốn đã hiện diện trong tài liệu gốc, nhưng **không sửa** các TODO về MRV, LCV, Forward Checking, Min-Conflicts; đó là công việc của các Bài 2–4.

`COUNT` của `backtrack_search` được ghi theo đúng định nghĩa của notebook gốc (số lượt gọi đệ quy, không đồng nghĩa số lần thử gán màu). Thời gian đo chỉ mang tính tham khảo.
