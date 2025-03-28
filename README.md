This is a simple expense tracker app that utilizes CLI to add, delete, list and summarize the user's expenses.

The followings commands are:

-add "<Description>" <amount>: adds a new expense, with a description (in-quotes) and an amount, which has to be a number, either an integer or float. The expense will have its own ID number, as well as a date of creation.

-delete <id>: deletes an expense by informing its own specific ID number, which can be found using the list command. Upon deletion, all expense ID numbers will be rearranged to retain the order.

-list: provides a simple list in table format, so the user can see all expenses, including the ID, date, description and amount.

-summary <month>: provides a summmary of the expenses, by adding the total expenses. This command can optionnally be filtered by month, using an integer number corresponding to that month (1 is January, 2 is February, 3 is March and so on).

Project URL: https://roadmap.sh/projects/expense-tracker
