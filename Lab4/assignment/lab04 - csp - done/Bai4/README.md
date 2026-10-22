# LAB04 – Bài 4: Forward Checking và Min-Conflicts

Bộ notebook kế thừa các Bài 1–3 từ `CSP_graph_coloring_example_Bai3_Hoan_thien(1).ipynb` và bổ sung Bài 4 ở cuối. Các phần gốc và hàm giảng viên được giữ nguyên; không ghi đè mã Backtracking cũ.

## Tệp chính

- `CSP_graph_coloring_example_Bai4_Hoan_thien.ipynb`: notebook có kết quả đã chạy; 62 cell, trong đó 29 cell Code.
- `CSP_graph_coloring_example_Bai4_Hoan_thien.html`: phiên bản đọc nhanh, chứa output.
- `Lab04_Bai1_Results/` … `Lab04_Bai3_Results/`: output kế thừa, được tạo lại khi chạy notebook.
- `Lab04_Bai4_Results/`: 5 bảng CSV và 4 hình PNG của Bài 4.
- `requirements.txt`: các thư viện cài đặt.

## Cách chạy

1. Mở terminal tại thư mục này, cài các gói từ `requirements.txt` (nếu cần).
2. Mở notebook bằng VS Code hoặc Jupyter Notebook/JupyterLab.
3. Chọn **Restart & Run All**. Thời gian có thể thay đổi theo phần cứng và máy đang chạy.
4. Các CSV và hình được xuất bằng đường dẫn tương đối vào thư mục `Lab04_Bai*_Results/`.

Không cần dữ liệu ngoài hay đường dẫn tuyệt đối. Sử dụng cùng đồ thị cho các thuật toán trong một lượt.

## Mô hình và quy ước đếm

- CSP: `variables`, `domains`, `constraints` (hai đầu cạnh phải khác màu).
- Forward Checking: gán màu, xóa màu của các hàng xóm chưa gán, phát hiện miền rỗng và **hoàn tác miền đầy đủ** khi backtrack.
- Min-Conflicts: phép gán **đầy đủ** khởi tạo ngẫu nhiên; mỗi bước nhận đổi màu làm **giảm nghiêm ngặt** số cạnh vi phạm. Tối đa 8 lần khởi tạo (7 lần restart) và 200 bước cải thiện mỗi lần.
- `COUNT`: số nút/ lần gọi đệ quy của Backtracking, kể cả nút gán đầy đủ; `attempts`: số lần thử gán màu; `steps`: số bước đổi màu thực sự được chấp nhận của Min-Conflicts; `value_evaluations`: số lần thử màu ứng viên. **Không so trực tiếp COUNT với steps.**
- `SOLVED`: có nghiệm kiểm chứng. `UNSAT`: Backtracking đã khảo sát hết nhánh mà không có nghiệm. `LIMIT`: thuật toán hết giới hạn tính toán và **chưa xác nhận vô nghiệm**. `STUCK`: Min-Conflicts không còn bước cải thiện được chấp nhận trong ngân sách, **không có nghĩa vô nghiệm**.

## Thiết lập thí nghiệm

- Đồ thị minh họa: Delaunay, n=10, seed=1111, 21 cạnh; có K4 nên ba màu vô nghiệm.
- Benchmark: `n ∈ {8,10,14,18,24}`, 5 seed/độ lớn, cùng đồ thị được so với 3 và 4 màu.
- Mỗi đồ thị/miền chạy ba thuật toán: MRV+LCV Backtracking có giới hạn an toàn, MRV+LCV+Forward Checking, Min-Conflicts strict.
- Hạt giống đồ thị: `20261020 + 100*n + trial`, với trial = 0...4. Min-Conflicts dùng seed đồ thị cộng 900001.
- Backtracking có `node_limit=10000`. Min-Conflicts có `max_steps=200`, `max_starts=8`.
- Ghi 150 lượt kết quả; tỷ lệ thành công trên 5 đồ thị và trung vị thời gian theo n.

## Kết quả trên đồ thị n=10 gốc

| Miền | Thuật toán | COUNT / steps | Trạng thái |
|---|---|---|---|
| 4 màu | MRV + LCV | COUNT=11 | SOLVED |
| 4 màu | MRV + LCV + FC | COUNT=11 | SOLVED |
| 4 màu | Min-Conflicts | steps=4 | SOLVED |
| 3 màu | MRV + LCV | COUNT=34 | UNSAT |
| 3 màu | MRV + LCV + FC | COUNT=28 | UNSAT |
| 3 màu | Min-Conflicts | steps=18 | STUCK |

## Các file Bài 4

| File | Ý nghĩa |
|---|---|
| `Bai4_Fixed_Graph_Comparison.csv` | Ba thuật toán trên cùng đồ thị 10 đỉnh (3/4 màu) |
| `Bai4_Delaunay_Instances.csv` | Số cạnh và seed của 25 đồ thị |
| `Bai4_Trial_Results.csv` | 150 bản ghi chi tiết theo đồ thị, miền và thuật toán |
| `Bai4_Summary_Results.csv` | Tỷ lệ thành công, số nút/bước, thời gian và tỷ lệ chứng minh vô nghiệm |
| `Bai4_Unit_Tests.csv` | Kiểm thử các bất biến của nghiệm và miền |
| `Bai4_Colored_Graph_FC_MinConflicts.png` | Đồ thị 4 màu do FC và Min-Conflicts tạo |
| `Bai4_Success_Rates.png` | Tỷ lệ nghiệm hợp lệ theo quy mô và miền màu |
| `Bai4_Runtime_vs_N.png` | Trung vị thời gian chạy theo n |
| `Bai4_Effort_COUNT_vs_Steps.png` | Hai thước đo công sức tìm kiếm tách riêng |

**Chú ý:** Kết quả về thời gian thực thi phụ thuộc phần cứng, phiên bản thư viện và tải hệ thống; không nên dùng số đo micro-benchmark làm chứng minh độ phức tạp. Ba màu *có thể* tô được trên một số đồ thị Delaunay, nhưng đồ thị có K4 chắc chắn phải dùng ít nhất bốn màu. Việc Min-Conflicts thất bại không được diễn giải là chứng minh vô nghiệm.
