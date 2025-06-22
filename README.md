# 📊 Daily Habit & Mood Tracker

Track your daily study, sleep, entertainment, and mood — all logged to a MySQL database, analyzed using Python, and beautifully visualized with graphs and PDF reports.

---

## 🚀 Features

- ✅ Log daily mood, study hours, sleep, entertainment, and topic studied  
- 🗃️ Store data in **MySQL** and backup to **CSV**  
- 📊 Generate visual dashboards using **Matplotlib** & **Seaborn**  
- 📄 Export professional **PDF summary reports**  
- 📂 Save all plots and reports to `assets/` folder  
- 💻 Menu-driven CLI interface (non-terminal display optional)

---

## 🛠️ Tech Stack

| Module         | Purpose                            |
|----------------|-------------------------------------|
| Python         | Core language                      |
| MySQL / PyMySQL| Database storage                   |
| Pandas         | Data processing                    |
| Matplotlib     | Plotting graphs                    |
| Seaborn        | Beautiful statistical plots        |
| FPDF           | PDF report generation              |
| OS / SYS       | File & directory handling          |

---

## 📂 Project Structure

```
habit-tracker/
│
├── main.py                 # Entry point & menu
├── logger.py               # Log daily habits
├── dashboard.py            # Data visualization & export
├── report_generator.py     # PDF summary generator
├── utils/
│   ├── db_connect.py       # MySQL connection handler
│   └── db_creation.py      # Table creation script
│
├── data/
│   └── daily_logs.csv      # Optional CSV backup
│
├── assets/
│   ├── mood_trend.png      # Saved graphs
│   └── habit_report.pdf    # Exported report
```

---

## 📸 Sample Visualizations

> All saved automatically to `assets/`

- Mood Trend Over Time  
- Average Time Allocation (Study, Sleep, Fun)  
- Correlation Heatmap (Mood vs Activities)  
- Bubble Chart: Study Hours vs Mood  
- Top 10 Keywords from Study Topics  

---

## 📄 Sample PDF Report

Includes:
- Summary Stats (Mood, Time Spent)
- Last 7 Days of Logs
- Optional charts (if extended)

---

## ▶️ Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/habit-tracker.git
   cd habit-tracker
   ```

2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your MySQL credentials in `utils/db_connect.py`

4. Run the program  
   ```bash
   python main.py
   ```

---

## 📌 Ideal For

- UG/PG Students learning Python & MySQL  
- Data Science beginners (applied statistics)  
- Resume project for internships or entry-level roles  
- Self-tracking enthusiasts

---

## 💡 Future Ideas

- Add login/auth system  
- Build a web dashboard (Flask/Streamlit)  
- Set weekly/monthly goals  
- Add notifications or email reports  

---

## 🧑‍💻 Author

Made with ❤️ by Jayanth R Sidlyali — a passionate Pythonista helping students use data to grow smarter.

---

## 📜 License

This project is licensed under the MIT License.
