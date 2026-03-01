
import json
import os
from datetime import datetime

DATA_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses, amount, category, description=''):
    expense = {
        'id': len(expenses) + 1,
        'amount': amount,
        'category': category,
        'description': description,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f'Expense added: {amount} in {category}')

def view_expenses(expenses):
    if not expenses:
        print('No expenses recorded yet.')
        return
    print('\n--- All Expenses ---')
    for expense in expenses:
        print(f"ID: {expense['id']}, Amount: {expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")
    print('--------------------')

def summarize_expenses(expenses):
    if not expenses:
        print('No expenses recorded yet.')
        return
    summary = {}
    for expense in expenses:
        category = expense['category'].lower()
        summary[category] = summary.get(category, 0) + expense['amount']
    
    print('\n--- Expense Summary by Category ---')
    for category, total in summary.items():
        print(f'{category.capitalize()}: {total:.2f}')
    print('-----------------------------------')

def main():
    expenses = load_expenses()

    while True:
        print('\nExpense Tracker Menu:')
        print('1. Add Expense')
        print('2. View Expenses')
        print('3. Summarize Expenses')
        print('4. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            try:
                amount = float(input('Enter amount: '))
                category = input('Enter category: ')
                description = input('Enter description (optional): ')
                add_expense(expenses, amount, category, description)
            except ValueError:
                print('Invalid amount. Please enter a number.')
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            summarize_expenses(expenses)
        elif choice == '4':
            print('Exiting Expense Tracker. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
