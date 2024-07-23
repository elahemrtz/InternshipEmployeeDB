import tkinter as tk

from database import select_query

class EmployeeSelectApp:
    def __init__(self, root, onselect=None):
        self.root = root
        self.onselect = onselect
        self.fetch_employees()
        self.create_widget()

    def create_widget(self):
        if len(self.employees) == 0:
            tk.Label(self.root, text='No Employees available!').pack(padx=10, pady=10)
        else:
            tk.Label(self.root, text="Select Employee:").pack(padx=10, pady=10)

            for user_id, user_name, user in self.employees:
                tk.Button(self.root,
                          text=f'{user_name} ({user_id})', 
                          command=lambda user=user: self.onselect(user))\
                    .pack(padx=10, pady=10)
            
    def fetch_employees(self):
        self.employees = []
        for emp in select_query('select * from employee_v1'):
            self.employees.append((emp[0], emp[7] + ' ' + emp[8], emp))

    