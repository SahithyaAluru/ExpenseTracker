import csv
import os
from datetime import datetime

data_file = "expenses.csv"

# Function to add an expense
def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category (Food, Transport, Entertainment, etc.): ").strip()
        description = input("Enter a brief description: ").strip()
        date = datetime.now().strftime("%Y-%m-%d")
        
        with open(data_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, amount, category, description])
        
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.\n")

# Function to view all expenses
def view_expenses():
    if not os.path.exists(data_file):
        print("No expenses recorded yet.\n")
        return
    
    with open(data_file, "r") as file:
        reader = csv.reader(file)
        print("\nDate          | Amount | Category      | Description")
        print("-" * 50)
        for row in reader:
            print(f"{row[0]:<12} | {row[1]:<6} | {row[2]:<12} | {row[3]}")
    print()

# Function to show expense summary
def expense_summary():
    if not os.path.exists(data_file):
        print("No expenses recorded yet.\n")
        return
    
    expenses = {}
    total = 0.0
    
    with open(data_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            amount = float(row[1])
            category = row[2]
            total += amount
            if category in expenses:
                expenses[category] += amount
            else:
                expenses[category] = amount
    
    print("\nExpense Summary")
    print("-" * 30)
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")
    print(f"Total Expenses: ${total:.2f}\n")

# Main menu loop
def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please select again.\n")

if __name__ == "__main__":
    main()
