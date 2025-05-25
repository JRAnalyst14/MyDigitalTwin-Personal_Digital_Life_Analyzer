import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from utils.db_connect import get_connection

def load_logs():
    conn = get_connection()
    query = "SELECT date, mood, study_hours, sleep_hours, entertainment_hours, topic FROM daily_log"
    df = pd.read_sql(query, conn)
    conn.close()
    df["date"] = pd.to_datetime(df["date"])
    return df

def save_plot(fig, filename):
    os.makedirs("assets", exist_ok=True)
    path = os.path.join("assets", filename)
    fig.savefig(path)
    plt.close(fig)
    print(f"📊 Saved: {path}")

def plot_mood_trend(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="date", y="mood", data=df, marker="o", color="green", ax=ax)
    ax.set_title("📈 Mood Trend Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Mood (1–10)")
    ax.grid(True)
    fig.tight_layout()
    save_plot(fig, "mood_trend.png")

def plot_time_allocation(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    avg_data = df[["study_hours", "sleep_hours", "entertainment_hours"]].mean()
    avg_data.plot(kind="bar", color=["blue", "orange", "purple"], ax=ax)
    ax.set_title("⏳ Average Time Spent Per Activity")
    ax.set_ylabel("Hours")
    ax.set_xticklabels(["Study", "Sleep", "Entertainment"], rotation=0)
    fig.tight_layout()
    save_plot(fig, "average_time.png")

def plot_correlation(df):
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(df[["mood", "study_hours", "sleep_hours", "entertainment_hours"]].corr(), 
                annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    ax.set_title("📊 Mood vs Activities Correlation")
    fig.tight_layout()
    save_plot(fig, "correlation_heatmap.png")

def plot_bubble(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(
        data=df,
        x="study_hours",
        y="mood",
        hue="sleep_hours",
        size="entertainment_hours",
        palette="viridis",
        sizes=(20, 200),
        ax=ax
    )
    ax.set_title("Study vs Mood (color=sleep, size=fun)")
    ax.grid(True)
    fig.tight_layout()
    save_plot(fig, "study_mood_bubble.png")

def plot_time_stacked(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    df_plot = df[["date", "study_hours", "sleep_hours", "entertainment_hours"]].set_index("date")
    df_plot.plot(kind="bar", stacked=True, colormap="Set3", ax=ax)
    ax.set_title("📅 Daily Time Allocation")
    ax.set_ylabel("Hours")
    ax.set_xlabel("Date")
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    save_plot(fig, "stacked_time.png")

def plot_top_topics(df):
    all_words = " ".join(df["topic"].fillna("").tolist())
    words = re.findall(r'\b\w{4,}\b', all_words.lower())
    common = Counter(words).most_common(10)
    
    if common:
        fig, ax = plt.subplots(figsize=(6, 4))
        words_df = pd.DataFrame(common, columns=["word", "count"])
        sns.barplot(x="count", y="word", data=words_df, palette="magma", ax=ax)
        ax.set_title("🧠 Top 10 Study Keywords")
        fig.tight_layout()
        save_plot(fig, "top_keywords.png")

def show_dashboard():
    df = load_logs()
    print("\n📊 Generating Dashboard...")

    plot_mood_trend(df)
    plot_time_allocation(df)
    plot_correlation(df)
    plot_bubble(df)
    plot_time_stacked(df)
    plot_top_topics(df)

    print("✅ Dashboard saved in 'assets/' folder.")
    print("📈 Summary Charts Generated Successfully!")