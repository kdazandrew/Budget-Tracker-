import os
import sys

class Application():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.expense_list = []
        self.expense_name = []
        self.income_name = []
        self.income_list = []
        self.prompt_income()

    def income_ask(self):
        add_income = input('Add income? [y/n]: ')
        return add_income

    def income_sum(self):
        self.income = sum(self.income_list)

    def expense_ask(self):
        add_expense = input('Add expense? [y/n]: ')
        return add_expense

    def expense_sum(self):
        self.expenses = sum(self.expense_list)

    def income_check(self):
        if not self.income_list:
            print('Please enter atleast one source of income. ')
            self.prompt_income()
        else:
            return

    def expense_check(self):
        if not self.expense_list:
            print('Please enter atleast one expense. ')
            self.prompt_expense()
        else:
