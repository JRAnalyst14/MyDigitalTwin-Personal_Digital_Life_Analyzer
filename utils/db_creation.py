import pymysql as ms

def create_database():
    connection = ms.connect(
        host='localhost',
        user="root",
        password="system"
    )
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS daily_habit_tracker")
        print("Database 'daily_habit_tracker' created or already exists.")
        cursor.execute("USE daily_habit_tracker")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS daily_log (
                id INT AUTO_INCREMENT PRIMARY KEY,
                date DATE NOT NULL,
                mood INT CHECK (mood BETWEEN 1 AND 10),
                study_hours FLOAT CHECK (study_hours >= 0),
                sleep_hours FLOAT CHECK (sleep_hours >= 0),
                entertainment_hours FLOAT CHECK (entertainment_hours >= 0),
                topic VARCHAR(255) NOT NULL
            )
        """)
        print("Table 'daily_log' created or already exists.")
        
    except ms.Error as e:
        print(f"Error creating database or table: {e}")
    finally:
        cursor.close()
        connection.close()