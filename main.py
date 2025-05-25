from system_scanner import scan_directory, save_to_csv
from habit_logger import log_habit
from report_generator import load_data
from dashboard import show_dashboard
from report_generator import generate_pdf, plot_summary_charts

def main():
    while True:
        print("\n MyDigitalTwin Digital Activity Tracker - Main Menu")
        print("1. Scan System Folder")
        print("2. Log Daily Habit")
        print("3. Generate Dashboard Report")
        print("4. Generate PDF Report")
        print("5. Exit")

        choice = input("Choose an option (1/2/3/4/5): ").strip()

        if choice == "1":
            folder = input("Enter folder path to scan (e.g. Downloads): ").strip()
            try:
                df = scan_directory(folder)
                print(f"Found {len(df)} files.")
                save_to_csv(df)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                log_habit()
            except Exception as e:
                print(f"Error logging habit: {e}")

        elif choice == "3":
            show_dashboard()

        elif choice == "4":
            df = load_data()
            plot_summary_charts(df) 
            generate_pdf(df)

        elif choice == "5":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
