# Advanced Artificial Intelligence

Repository lưu trữ bài tập theo tuần của học phần **Trí tuệ nhân tạo nâng cao**.

**Sinh viên:** Đào Duy Hưng  
**MSSV:** 3122410158

## Mục tiêu học tập

Các bài thực hành trong repository tập trung vào việc xây dựng và đánh giá **tác tử thông minh** trong các môi trường mô phỏng. Nội dung đặt nền tảng cho các chủ đề nâng cao hơn, bao gồm học tăng cường (*reinforcement learning*): quan sát môi trường, lựa chọn hành động, đánh giá hiệu năng và cải thiện chính sách tác tử.

> Lưu ý: Mã nguồn hiện tại chủ yếu triển khai tác tử phản xạ và tác tử dựa trên mô hình; chưa bao gồm các thuật toán học tăng cường như Q-learning hoặc DQN.

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

3. Mở notebook trong thư mục `Lab1/` và chạy lần lượt các cell.

Với các bài có trực quan hóa hoặc ghi hình môi trường Gymnasium, notebook có thể cần thêm các phụ thuộc hiển thị phù hợp với hệ điều hành đang dùng.

## Tài liệu tham khảo

- Stuart Russell & Peter Norvig, *Artificial Intelligence: A Modern Approach*, 4th Edition.
- M. Hahsler, tài liệu và notebook mẫu về Intelligent Agents.
- Liu (2024), *AlphaGo Simplified: Rule-Based AI and Deep Learning in Everyday Games*.

## Ghi chú học thuật

Repository được dùng cho mục đích học tập. Mỗi notebook cần được đọc, chạy thử và hiểu rõ trước khi sử dụng làm bài nộp. Một số tài liệu/notebook mẫu trong Lab 1 có ghi nhận giấy phép và tác giả gốc trong thư mục tương ứng.
