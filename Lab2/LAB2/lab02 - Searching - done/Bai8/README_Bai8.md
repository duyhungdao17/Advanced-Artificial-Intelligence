# Bài 8 — Goal-based Planning Agent — Hướng dẫn và kết quả

## Tệp tin

- `Ex1_Maze_Bai8_Hoan_thien.ipynb`: bài thực hành chính (BFS, DFS, GBFS, A*, so sánh 8 mê cung, IDS, nhiều đích).
- `Ex2_Maze_simplified_Bai8_Hoan_thien.ipynb`: bài thực hành rút gọn (BFS trên 4 mê cung).
- Hai file `.html` tương ứng: báo cáo có sẵn mã nguồn và toàn bộ output/hình đã chạy.
- `maze_helper.py` và 8 file `*_maze.txt`: phụ thuộc của notebook và dữ liệu. Không cần Internet khi chạy.
- Ba file `ket_qua_*.csv`: kết quả các thử nghiệm; 4 file `hinh_*.png`: hình minh họa.

## Cách chạy

1. Giải nén tất cả file vào **cùng một thư mục**.
2. Mở hai notebook trong VS Code/Jupyter Lab/Jupyter Notebook rồi chọn `Restart & Run All`.
3. Khai tên, MSSV và xác nhận khai báo công cụ hỗ trợ trên trang đầu trước khi nộp.
4. Các cell xuất CSV và hình sẽ ghi kết quả vào thư mục đang làm việc. `max_memory` là số Node/proxy đối tượng, **không phải số byte RAM thực đo**.
5. Bản HTML có output đã chạy, có thể mở trên trình duyệt để tham khảo hoặc nộp khi cần.

## Các ràng buộc quan trọng

- Bản đồ gốc không bị sửa bởi bất kỳ thuật toán tìm kiếm nào. Chỉ sao chép khi vẽ hình hoặc tạo bản đồ nhiều đích.
- `DFS` chỉ kiểm tra chu trình trên **nhánh hiện tại**, không dùng bảng `reached` toàn cục. Trường hợp bị giới hạn được ghi `LIMIT_REACHED`, **không phải** vô nghiệm.
- `IDS` chạy lặp DLS và bị giới hạn số lần mở rộng để notebook có thể hoàn thành ổn định; một số bản đồ có thể hiện `LIMIT_REACHED` do tổ hợp đường đi quá lớn.
- `BFS`, `A*` bảo đảm đường đi tối ưu trong mô hình 4 hướng, mỗi bước chi phí 1; GBFS/DFS không bảo đảm tối ưu.
- Mọi test `FOUND` được kiểm chứng bằng cách chạy lại chuỗi hành động qua lưới; A* được đối chiếu độ dài với BFS ở tất cả 8 mê cung.

## Bảng chi phí đường đi (8 mê cung × 4 thuật toán)

| Maze         |   A* |   BFS |   DFS |   GBFS |
|:-------------|-----:|------:|------:|-------:|
| small        |   19 |    19 |    37 |     29 |
| medium       |   68 |    68 |   244 |     74 |
| large        |  210 |   210 |   210 |    210 |
| open         |   54 |    54 |   nan |     68 |
| L            |   16 |    16 |    50 |     24 |
| loops        |   23 |    23 |    41 |     35 |
| empty        |   14 |    14 |    34 |     14 |
| empty_maze_2 |   14 |    14 |    80 |     14 |

Dấu trống tại `open / DFS` là do giới hạn 20.000 nút mở rộng, không phải không có lời giải.

## IDS — thông tin về giới hạn

| Maze         | Status        |   Path_cost |   Iterations |   Limit_increases |   Total_expanded |
|:-------------|:--------------|------------:|-------------:|------------------:|-----------------:|
| small        | FOUND         |          19 |           20 |                19 |             1051 |
| medium       | LIMIT_REACHED |         nan |           63 |                62 |            12000 |
| large        | LIMIT_REACHED |         nan |           95 |                94 |            12000 |
| open         | LIMIT_REACHED |         nan |           10 |                 9 |             5555 |
| L            | LIMIT_REACHED |         nan |            8 |                 7 |             4828 |
| loops        | LIMIT_REACHED |         nan |           17 |                16 |             8326 |
| empty        | LIMIT_REACHED |         nan |            9 |                 8 |             5060 |
| empty_maze_2 | LIMIT_REACHED |         nan |            9 |                 8 |             5060 |

## Phần nhiều đích

Trên bản sao `medium_maze`, thêm 2 đích (tổng 3 đích): BFS và IDS tìm lời giải 4 bước, DFS tìm lời giải 84 bước trong thứ tự N-E-S-W. Đây là ví dụ DFS không tối ưu.

## Khuyến nghị khi sử dụng báo cáo

Đọc từng cell, nắm được cách cập nhật frontier/reached và diễn giải đúng các chỉ số thực nghiệm. Cần bổ sung thông tin sinh viên và điều chỉnh nhận xét bằng hiểu biết của bản thân.
