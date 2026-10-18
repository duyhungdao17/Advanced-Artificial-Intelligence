# Advanced Artificial Intelligence

Repository lưu trữ bài tập theo tuần của học phần **Trí tuệ nhân tạo nâng cao**.

**Sinh viên:** Đào Duy Hưng  
**MSSV:** 3122410158

## Mục tiêu học tập

Các bài thực hành trong repository tập trung vào **tác tử thông minh** và **giải quyết vấn đề bằng tìm kiếm**. Nội dung gồm quan sát môi trường, lựa chọn hành động, so sánh chiến lược tìm kiếm và đánh giá hiệu năng; đây là nền tảng cho các chủ đề nâng cao hơn như học tăng cường (*reinforcement learning*).

> Lưu ý: Repository hiện có các bài về tác tử và thuật toán tìm kiếm; chưa bao gồm các thuật toán học tăng cường như Q-learning hoặc DQN.

## Cấu trúc repository

```text
.
├── Lab0/
│   └── bt01_discussion_daoduyhung_3122410158.docx
├── Lab1/
│   ├── robot_vacuum.ipynb
│   ├── lunar_lander.ipynb
│   ├── gridhunt_mini_assignment.ipynb
│   ├── gridhunt_multiagent_mini_assignment.ipynb
│   ├── gridhunt.png
│   └── lab01 - Agent/
│       ├── README.md
│       ├── gymnasium_display_recorder.py
│       ├── videos/
│       └── các notebook và tài nguyên của Lab 1
├── Lab2/
│   ├── EX1/                          # Bài tập tìm kiếm heuristic và bài giải
│   └── LAB2/
│       ├── lab02 - Searching/        # Notebook và dữ liệu mẫu
│       ├── lab02 - Searching - done/ # Bài thực hành theo từng bài
│       └── lab02_search_DaoDuyHung_3122410158/
│           ├── README.md
│           ├── 01_Report/
│           ├── 02_Notebooks/
│           ├── 03_Source_Data/
│           └── 04_Results/
├── Lab3/
│   ├── Theory/                       # Bài tập CSP
│   └── Lab/
│       ├── lab03 - local search/     # Notebook và dữ liệu mẫu
│       ├── lab03 - solution/         # Lời giải từng bài
│       └── lab03_localsearch_search_daoduyhung_3122410158/
│           ├── 1_Report/
│           ├── 2_Notebooks/
│           ├── 3_Data/
│           ├── 4_Images/
│           └── 5_Supports/
├── Artificial Intelligence A Modern Approach 4th.pdf
└── 2024 - Liu - AlphaGo Simplified Rule-Based AI and Deep Learning in Everyday Games.pdf
```

## Nội dung bài tập

### Lab 0 — Thảo luận

- Bài thảo luận nền tảng của học phần.

### Lab 1 — Intelligent Agents

- **Robot Vacuum:** mô phỏng robot hút bụi và so sánh các chiến lược tác tử phản xạ, dựa trên mô hình.
- **Lunar Lander:** xây dựng tác tử điều khiển môi trường Lunar Lander với Gymnasium.
- **GridHunt:** thiết kế tác tử thợ săn trong môi trường lưới; thực hành quan sát, ghi nhớ trạng thái và ra quyết định.
- **GridHunt Multi-Agent:** mở rộng GridHunt sang môi trường nhiều tác tử.

### Lab 2 — Problem Solving by Search

- **EX1:** bài tập về tìm kiếm AI, tìm kiếm heuristic và bài giải dạng PDF.
- **LAB2:** thực hành tìm kiếm trên cây và mê cung; so sánh BFS, DFS, A*, tìm kiếm theo độ sâu và các heuristic.
- Bài làm tổng hợp gồm [báo cáo, notebook, dữ liệu và kết quả thực nghiệm](Lab2/LAB2/lab02_search_DaoDuyHung_3122410158/README.md).

### Lab 3 — Local Search

- **Theory:** bài tập về bài toán thỏa mãn ràng buộc (CSP).
- **Lab:** áp dụng tìm kiếm cục bộ cho mê cung, n-Queens và bài toán người du lịch (TSP); thực nghiệm hill climbing, random restart, simulated annealing và các lịch giảm nhiệt.
- [Bài làm tổng hợp](Lab3/Lab/lab03_localsearch_search_daoduyhung_3122410158/) gồm báo cáo PDF, notebook, dữ liệu CSV, biểu đồ và tệp hỗ trợ. [Lời giải từng bài](Lab3/Lab/lab03%20-%20solution/) nằm trong các thư mục `Bai1` đến `Bai8`.

## Yêu cầu môi trường

- Python 3.10+ (notebook hiện có dùng Python 3.12)
- Jupyter Notebook hoặc JupyterLab
- Các thư viện chính: `numpy`, `matplotlib`, `gymnasium`, `ipython`

Cài đặt các thư viện cần thiết:

```bash
pip install jupyter numpy matplotlib gymnasium
```

## Cách chạy

1. Clone repository:

   ```bash
   git clone https://github.com/duyhungdao17/Advanced-Artificial-Intelligence.git
   cd Advanced-Artificial-Intelligence
   ```

2. Mở Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Mở notebook trong `Lab1/`, `Lab2/LAB2/lab02_search_DaoDuyHung_3122410158/02_Notebooks/` hoặc `Lab3/Lab/lab03_localsearch_search_daoduyhung_3122410158/2_Notebooks/` và chạy lần lượt các cell. Với Lab 2, đặt thư mục làm việc tại `02_Notebooks` để notebook tìm thấy các tệp `.py` và `.txt` đi kèm. Với Lab 3, xem thêm tệp hỗ trợ trong `5_Supports/`.

Các phụ thuộc chung cho Lab 3 được liệt kê trong [requirements.txt](Lab3/Lab/lab03_localsearch_search_daoduyhung_3122410158/5_Supports/requirements.txt):

```bash
pip install -r Lab3/Lab/lab03_localsearch_search_daoduyhung_3122410158/5_Supports/requirements.txt
```

Bài 6 cần thêm `numba`; Bài 7 cần thêm `scipy`. Xem README và requirements riêng trong từng thư mục bài giải để chạy lại các thí nghiệm.

Với các bài có trực quan hóa hoặc ghi hình môi trường Gymnasium, notebook có thể cần thêm các phụ thuộc hiển thị phù hợp với hệ điều hành đang dùng.

## Tài liệu tham khảo

- Stuart Russell & Peter Norvig, *Artificial Intelligence: A Modern Approach*, 4th Edition.
- M. Hahsler, tài liệu và notebook mẫu về Intelligent Agents.
- Liu (2024), *AlphaGo Simplified: Rule-Based AI and Deep Learning in Everyday Games*.

## Ghi chú học thuật

Repository được dùng cho mục đích học tập. Mỗi notebook cần được đọc, chạy thử và hiểu rõ trước khi sử dụng làm bài nộp. Một số tài liệu/notebook mẫu trong Lab 1 có ghi nhận giấy phép và tác giả gốc trong thư mục tương ứng.
