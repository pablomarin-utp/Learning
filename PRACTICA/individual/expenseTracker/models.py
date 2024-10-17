class Expense: 

    def __init__(self, id, description, amount, date, type): 
        self.id = id
        self.description = description
        self.amount = amount
        self.date = date
        self.type = type

    def delete(self):
        expenses = Expense.get_all()
        expenses.remove(self)
        Expense.save_all(expenses)
    
    def make_report(self):
        print("Expense: ", self.description)
        print("Amount: ", self.amount)
        print("Date: ", self.date)
        print("Type: ", self.type)

