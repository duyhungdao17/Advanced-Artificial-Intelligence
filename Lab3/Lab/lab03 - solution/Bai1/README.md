# Lab03 – Bài 1: Simple Hill Climbing trên L-maze

## File
- `Maze_Example_LocalSearch_Bai1_Hoan_thien.ipynb`: 12 cell gốc giữ nguyên + các cell Code/Markdown bổ sung.
- `L_maze.txt`: dữ liệu mê cung theo giảng viên.
- `maze_helper.py`: module hỗ trợ hiển thị/animation của bộ thực hành.
- `Lab03_Bai1_Experiment_Results.csv`: kết quả sau khi chạy notebook.
- `Lab03_Bai1_HillClimbing_Results.png`: hình xuất từ notebook.

## Cách chạy
Giữ notebook, `L_maze.txt` và `maze_helper.py` trong cùng thư mục. Cài `numpy matplotlib pandas ipython ipykernel` nếu cần; mở Jupyter hoặc VS Code và chọn **Restart & Run All**. Cell tải dữ liệu ở đầu chỉ tải nếu không có file, nên có thể chạy ngoại tuyến.

## Giải thích kết quả
Simple Hill Climbing ở notebook gốc dùng `min(obj)` trên toàn bộ lân cận (best-improvement). Dừng tại (5,9), chưa đạt G=(2,12), do điểm cực tiểu cục bộ; BFS vẫn tìm được đường 16 bước. `result["solution"]` là tọa độ kết thúc chứ không phải đảm bảo có nghiệm.
