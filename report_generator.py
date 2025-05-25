import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from utils.db_connect import get_connection

def load_data():
    conn = get_connection()
    query = "SELECT * FROM daily_log ORDER BY date ASC"
    df = pd.read_sql(query, conn)
    conn.close()
    df["date"] = pd.to_datetime(df["date"])
    return df

def plot_summary_charts(df):
    os.makedirs("assets", exist_ok=True)

    plt.figure(figsize=(6, 3))
    plt.plot(df["date"], df["mood"], marker="o", color="green")
    plt.title("Mood Trend")
    plt.xlabel("Date")
    plt.ylabel("Mood")
    plt.grid(True)
    plt.tight_layout()
    mood_path = "assets/mood_trend.png"
    plt.savefig(mood_path)
    plt.close()

    plt.figure(figsize=(4, 3))
    df[["study_hours", "sleep_hours", "entertainment_hours"]].mean().plot(
        kind="bar", color=["blue", "orange", "purple"]
    )
    plt.title("Average Time Allocation")
    plt.xticks(rotation=0)
    plt.tight_layout()
    time_path = "assets/time_allocation.png"
    plt.savefig(time_path)
    plt.close()

    return mood_path, time_path

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Weekly Habit Report", ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 8, title, ln=True)
        self.ln(4)

    def section_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

def generate_pdf(df):
    os.makedirs("assets", exist_ok=True)
    pdf = PDF()
    pdf.add_page()

    avg_mood = round(df["mood"].mean(), 2)
    total_study = df["study_hours"].sum()
    total_sleep = df["sleep_hours"].sum()
    total_ent = df["entertainment_hours"].sum()

    pdf.section_title("Summary")
    summary = (
        f"Records Logged: {len(df)}\n"
        f"Average Mood: {avg_mood}/10\n"
        f"Total Study Hours: {total_study}\n"
        f"Total Sleep Hours: {total_sleep}\n"
        f"Total Entertainment Hours: {total_ent}"
    )
    pdf.section_body(summary)

    # Recent Logs Section
    pdf.section_title("Recent Logs")
    last_entries = df.tail(7)
    for _, row in last_entries.iterrows():
        line = (
            f"{row['date'].strftime('%Y-%m-%d')}: "
            f"Mood={row['mood']}, Studied={row['study_hours']}h, "
            f"Slept={row['sleep_hours']}h, Fun={row['entertainment_hours']}h, "
            f"Topic={row['topic']}"
        )
        pdf.section_body(line)

    # Save PDF
    pdf_path = "assets/habit_report.pdf"
    pdf.output(pdf_path)
    print(f"📄 Report saved to: {pdf_path}")
