# LAB04 — Bài 2: Kiểm tra tính đầy đủ và nhất quán

## Nội dung

Notebook `CSP_graph_coloring_example_Bai2_Hoan_thien.ipynb` kế thừa đầy đủ Bài 1 (sinh đồ thị bằng Delaunay, seed = 1111, n = 10) và bổ sung Markdown/Code cho Bài 2.

- Giữ nguyên `complete()` và `consistent()` của notebook do giảng viên cung cấp.
- Kiểm tra `csp['variables']`, `csp['domains']`, `csp['constraints']`.
- Kiểm thử 8 trường hợp: rỗng, từng phần hợp lệ, hai đỉnh kề khác màu, hai đỉnh kề cùng màu, đầy đủ nhưng xung đột, tô 4 màu hợp lệ, màu ngoài miền và tô 3 màu xung đột.
- Đối chiếu kết quả thực tế với kết quả mong đợi qua `assert`; xuất CSV và hình.
- Ghi rõ giới hạn của `consistent()` gốc: chỉ xét ràng buộc cạnh, **không xác nhận màu thuộc miền D**. Thêm `domain_valid()`/`is_csp_solution()` riêng, không ghi đè hai hàm gốc.
- Giữ nguyên các TODO về MRV, LCV, Forward Checking và Min-Conflicts dành cho Bài 3–4.

## Kết quả

- Đồ thị: 10 đỉnh, 21 cạnh không hướng.
- 8/8 kiểm thử PASS.
- Tô 4 màu có nghiệm hợp lệ; tô 3 màu trên đồ thị cố định này không có nghiệm do chứa K4 (đã xác nhận ở Bài 1).
- Phép gán đầy đủ tất cả đỉnh màu đỏ vi phạm 21 cạnh.

## Cấu trúc

```
Lab04_Bai2_CSP/
  CSP_graph_coloring_example_Bai2_Hoan_thien.ipynb
  CSP_graph_coloring_example_Bai2_Hoan_thien.html
  Lab04_Bai1_Results/
    Bai1_CSP_Domain_Comparison.csv
    Bai1_CSP_Neighbors.csv
    Bai1_CSP_Edges.csv
    Bai1_Delaunay_Graph_K4.png
    Bai1_Valid_Four_Coloring.png
  Lab04_Bai2_Results/
    Bai2_CSP_Completeness_Consistency_Tests.csv
    Bai2_CSP_Assignment_Examples.png
  requirements.txt
  README.md
```

## Cách chạy

1. Mở notebook bằng Jupyter Notebook / JupyterLab / VS Code.
2. Cài thư viện khi cần: `pip install -r requirements.txt`.
3. Chọn **Restart & Run All**; chạy theo thứ tự cell.
4. Kết quả được xuất bằng đường dẫn tương đối vào `Lab04_Bai1_Results/` và `Lab04_Bai2_Results/`.

Không cần thay đường dẫn theo máy cá nhân. Thí nghiệm Bài 2 dùng nghiệm 4 màu của Bài 1, vì vậy bắt buộc chạy tuần tự các cell.
