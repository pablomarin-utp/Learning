from models import Expense
from models import check_type, check_amount, check_date, types
from utils import show_types

def init():
    global expenses_db
    print("Which kind of expense do you want to register?")
    show_types(types)
    
    type = input("Type: ")
    if not check_type(type, types):
        return

    description = input("Description: ")

    amount = input("Amount: ")
    if not check_amount(amount):
        return

    date = input("Date (YYYY-MM-DD): ")
    if not check_date(date):
        return

    id = len(expenses_db)
    expense = Expense(id, description, amount, date, type)
    expenses_db.append(expense)
    print("Expense registered")
    return expense

def show_all():
    for expense in expenses_db:
        print("-------------")
        expense.make_report()
    print("-------------")

if __name__ == "__main__":
    expenses_db = []

    while True:
        print("What do you want to do?")
        print("1. Register expense")
        print("2. Show all expenses")
        print("3. Exit")
        option = input("Option: ")
        if option == "1":
            init()
        elif option == "2":
            show_all()
        elif option == "3":
            break
        else:
            print("Invalid option")
