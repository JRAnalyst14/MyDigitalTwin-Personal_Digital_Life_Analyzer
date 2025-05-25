import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="system",
        database="daily_habit_tracker"
    )
