# Lab02 – Bài 5: GBFS, A* và Weighted A*

## Cách chạy

Giải nén các file trong cùng một thư mục, mở lần lượt:
- `02_Maze_Example_Bai5_Hoan_thien.ipynb` (giữ nguyên nội dung Bài 3–4 đã hoàn thiện, thêm Bài 5).
- `04_Maze_BFS_vs_A_Star_Bai5_Hoan_thien.ipynb` (giữ nguyên cell gốc, thêm so sánh BFS/A*).

Trong VS Code / Jupyter: `Restart & Run All`. Google Colab: tải cả `.py` và các `.txt` lên cùng thư mục hoặc mount Drive. Các package thường dùng: numpy, pandas, matplotlib, notebook/ipykernel, IPython.

## Bộ dữ liệu và bảng

- 8 mê cung `.txt`: small, medium, large, open, L, loops, empty, empty_maze_2.
- `maze_helper.py` dùng để parse / hiển thị mê cung.
- `tree_search_solution.py` là phiên bản hỗ trợ **được tự cài đặt cho bài thực hành**, không phải mã gốc chưa được phát hành của tác giả. File này được bổ sung hàm `euclidean()` để notebook `04` chạy được.
- Hai file CSV dùng cho báo cáo và đối chiếu số liệu; thời gian đo thực thi đã lưu trong các notebook, không coi là giá trị cố định giữa các máy.
- Hai hình `.png` dùng minh họa đường đi và vùng trạng thái mở rộng.

## Thiết lập

4 hướng NESW, chi phí mỗi bước 1, thứ tự sinh cố định NESW. `Nodes expanded` không bao gồm nút đích vừa lấy khỏi frontier. `Max frontier` là số phần tử lớn nhất trong danh sách chờ. 

## Lưu ý học thuật

Các con số chỉ đúng với dữ liệu, cài đặt, quy tắc phá hòa của bộ mã kèm theo. Chỉ số `nút mở rộng` không đồng nhất tuyệt đối với `số trạng thái khác nhau` nếu có mở rộng lại cùng trạng thái. Weighted A* với w>1 không đảm bảo tối ưu và việc tăng w không đảm bảo tốc độ tăng đơn điệu.
