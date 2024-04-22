import tkinter as tk
from tkinter import messagebox
import random 
class BusinessManagementGame:
    def _init_(self, master):
        self.master=master
        self.master.title(BusinessManagementGame)
        self.balance=1000
        self.expenses=500
        self.income=0
        self.create_widgets()
    def create_widgets(self):
        self.balance_label=tk.Label(self.master, text=f"Balance:${self.balance}")
        self.balance_label.pack()
        self.expenses_label=tk.Label(self.master, text=f"Expenses:${self.expenses}")
        self.expenses_label.pack()
        self.income_label=tk.Label(self.master, text=f"Income:${self.income}")
        self.income_label.pack()
        self.invert_button=tk.Button(self.master, text="invest", command=self.invest)
        self.invert_button.pack()
        self.work_button=tk.Button(self.master, text="work", command=self.work)
        self.work_button.pack()

    def invest(self):
            investment=random.randint(100,500)
            self.balance-=investment
            self.expenses+=investment
            self.update_display()

    def work(self):
                income=random.randint(200,800)
                self.balance+=income
                self.income+=income
                self.update_display()
                if self.income>=self.expenses:
                    messagebox.showinfo("congratulation","you have earned enough money to cover your exxpenses")

    def update_display(self):
               self.balance_label.config(text=f"Balance:${self.balance}")
               self.expenses_label.config(text=f"Expenses:${self.expenses}")
               self.income_label.config(text=f"Income:${self.income}")

if _name=="main_":
        root=tk.Tk()
        app=BusinessManagementGame(root)
        root.mainloop()