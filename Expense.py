import pandas as pd
import os
from datetime import datetime

# Constants
FILENAME = 'expenses.csv'
PASSWORD = '1234'  # You can change this

# Create CSV file with headers if it doesn't exist
if not os.path.exists(FILENAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df.to_csv(FILENAME, index=False)

# Load expenses
def load_data():
    return pd.read_csv(FILENAME)

# Save expense
def save_expense(date, category, amount, description):
    new_data = pd.DataFrame([[date, category, amount, description]],
                            columns=["Date", "Category", "Amount", "Description"])
    new_data.to_csv(FILENAME, mode='a', header=False, index=False)

# Add new expense
def add_expense():
    date = input("📅 Enter date (YYYY-MM-DD) or leave blank for today: ")
    if date == "":
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("📂 Enter category (Food, Rent, etc): ")
    amount = float(input("💰 Enter amount: "))
    description = input("📝 Enter description: ")
    save_expense(date, category, amount, description)
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    df = load_data()
    print(df)

# Total expenses
def total_expenses():
    df = load_data()
    print(f"💵 Total Expenses: ₹{df['Amount'].sum()}")

# Filter by category
def filter_by_category():
    df = load_data()
    cat = input("Enter category to filter: ")
    filtered = df[df['Category'].str.lower() == cat.lower()]
    print(filtered)

# Filter by date range
def filter_by_date_range():
    df = load_data()
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    df['Date'] = pd.to_datetime(df['Date'])
    filtered = df[(df['Date'] >= start) & (df['Date'] <= end)]
    print(filtered)

# Monthly report
def monthly_report():
    df = load_data()
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    report = df.groupby('Month')['Amount'].sum().reset_index()
    print("📊 Monthly Expense Report:\n", report)

# Top 3 expenses
def top_expenses():
    df = load_data()
    top3 = df.sort_values(by='Amount', ascending=False).head(3)
    print("🔥 Top 3 Highest Expenses:\n", top3)

# Export filtered data
def export_filtered():
    df = load_data()
    cat = input("Enter category to export: ")
    filtered = df[df['Category'].str.lower() == cat.lower()]
    file_name = f"{cat.lower()}_expenses.csv"
    filtered.to_csv(file_name, index=False)
    print(f"✅ Filtered data exported to {file_name}")

# Password protection
def authenticate():
    attempts = 3
    while attempts > 0:
        pwd = input("🔐 Enter password to access Expense Tracker: ")
        if pwd == PASSWORD:
            print("🔓 Access Granted!\n")
            return True
        else:
            attempts -= 1
            print(f"❌ Wrong password. {attempts} attempts left.")
    print("⛔ Access Denied.")
    return False

# Main menu
def main_menu():
    while True:
        print("\n====== 💼 Expense Tracker Menu ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expenses")
        print("4. Filter by Category")
        print("5. Filter by Date Range")
        print("6. Monthly Report")
        print("7. Top 3 Expenses")
        print("8. Export Filtered Data")
        print("9. Exit")
        choice = input("Choose an option (1-9): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            filter_by_category()
        elif choice == '5':
            filter_by_date_range()
        elif choice == '6':
            monthly_report()
        elif choice == '7':
            top_expenses()
        elif choice == '8':
            export_filtered()
        elif choice == '9':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

# Run with password check
if authenticate():
    main_menu()
