import json
import datetime
import shlex
from tabulate import tabulate

file_path = "expenses.json"
expenses = {}

def addExpense(description, amount):
    global expenses
    if amount == int or amount == float:
        if expenses:
            id = max([int(key) for key in expenses.keys()]) + 1
        else:
            id = 1

        expense = {
            "ID" : id,
            "Date" : datetime.datetime.now().strftime("%Y-%m-%d"),
            "Description" : description,
            "Amount" : amount
        }

        expenses[str(id)] = expense

        with open(file_path, "w") as json_file:
            json.dump(expenses, json_file, indent=4)

        print(f"Expense added successfully (ID:{id})")
    else:
        print("Invalid amount. Please enter a valid number.")
    return id

def deleteExpense(id):
    global expenses
    
    if id in expenses:
        del expenses[id]
        print("Expense deleted successfully.")

        new_expenses = {}
        for new_id, old_id in enumerate(sorted(expenses.keys(), key=int), start=1):
            expense = expenses[old_id]
            expense['ID'] = new_id
            new_expenses[str(new_id)] = expense

        expenses.clear()
        expenses.update(new_expenses)

        with open(file_path, "w") as json_file:
            json.dump(expenses, json_file, indent=4)

    else:
        print(f"ID number {id} not found.")

def expenseList():
    found = False
    table_data = []

    if expenses != {}:
        for value in expenses.values():
            row = [value.get("ID"), value.get("Date"), value.get("Description"), "$" + value.get("Amount")]
            table_data.append(row)

        print(tabulate(table_data, headers=["ID", "Date", "Description", "Amount"]))
    else:
        print("No expenses found.")

def expenseSummary(month = None):
    global expenses
    total_expenses = 0
    months = {
        "1" : "January",
        "2" : "February",
        "3" : "March",
        "4" : "April",
        "5" : "May",
        "6" : "June",
        "7" : "July",
        "8" : "August",
        "9" : "September",
        "10" : "October",
        "11" : "November",
        "12" : "December"
    }

    if month == None:
        for values in expenses.values():
            total_expenses += int(values.get('Amount'))
        print(f"Total expenses: ${total_expenses}")
    elif str(month) in months.keys():
        for expense in expenses.values():
            date = expense.get("Date")
            if date and date[5:7] == str(month).zfill(2):
                total_expenses += int(expense.get('Amount'))
        print(f"Total expenses for {months.get(str(month))}: ${total_expenses}")
    else:
        print("Invalid month provided.")

commands = {
    "add" : addExpense,
    "delete" : deleteExpense,
    "list" : expenseList,
    "summary" : expenseSummary
}

def userCommands(user_input):
    split_input = shlex.split(user_input)
    command_func = commands.get(split_input[0])

    if command_func:
        try:
            command_func(*split_input[1:])
        except:
            print("Error running the command, is it written correctly?")
    else:
        print("Invalid command.")

with open(file_path, "r") as json_file: #loads data from JSON file
    try:
        expenses = json.load(json_file)
        print("Data successfully loaded.")
    except json.JSONDecodeError:
        tasks = {}
        print("The JSON file is empty or not properly formatted.")


while True:
    user_input = input("expense-tracker ")
    userCommands(user_input)
