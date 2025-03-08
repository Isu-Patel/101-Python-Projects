import csv
from datetime import datetime

from matplotlib import category

# File Name for Storing Expense Data
file_name = 'ExpenseData.csv'

# Function to add an expense
def add_expenses():
    try:
        date = input('Enter the date of the expense (YYYY-MM-DD): ')
        category = input('Enter the category of the expense: ')
        description = input('Enter the description of the expense: ')
        amount = float(input('Enter the amount of the expense: '))

        # Save Expense to CSV File
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])
        print("Expense Added Successfully!")

    except Exception as e:
        print(f"An error occurred: {e}. Enter a valid amount.")


# Function to view all expenses
def view_expenses():
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            print(f"{'Date':<12} {'Category':<15} {'Description':<25} {'Amount':<10}")
            print("_" * 65) 
            for row in reader:
                print(f"{row[0]:<12} {row[1]:<15} {row[2]:<25} {row[3]:<10}")
    except FileNotFoundError:
        print("No expense data found. Please add some expenses first.")

# Main Menu
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expenses()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting the Expense Tracker...")
            break
        else:
            print("Invalid Choice. Please enter a valid choice.")

if __name__ == '__main__':
    main()

# ---------------------------- Output ---------------------------- #
# Expense Tracker
# 1. Add Expense
# 2. View Expenses
# 3. Exit
# Enter your choice: 1
# Enter the date of the expense (YYYY-MM-DD): 2021-10-01
# Enter the category of the expense: Grocery
# Enter the description of the expense: Vegetables
# Enter the amount of the expense: 100
# Expense Added Successfully!
