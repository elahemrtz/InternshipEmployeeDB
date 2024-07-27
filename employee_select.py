import calendar
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from typing import Dict

from database import select_query
from timesheet import TimesheetCreateApp, TimesheetViewApp

class EmployeeSelectApp:
    def __init__(self, root, for_salary=False):
        self.root = root
        self.for_salary = for_salary
        self.fetch_employees()
        self.create_widget()

    def create_widget(self):
        if len(self.employees) == 0:
            tk.Label(self.root, text='No Employees available!').pack(padx=10, pady=10)
        else:
            statuses: Dict[int, tk.Label] = {}
            def refresh():
                for user_id, percenteage, rem_count in self.get_overall_timesheet_status():                    
                    statuses[user_id]['text'] = f'{percenteage * 100:.2f}% Verified ({rem_count} Remaining)'

            if self.for_salary:
                now = datetime.now()
                self.year_var = tk.IntVar(value=now.year)
                tk.Label(self.root, text='Year').grid(row=1, column=1, padx=10, pady=5)
                ttk.Combobox(
                    self.root,
                    state="readonly",
                    values= list(range(now.year-10, now.year+1))[::-1],
                    textvariable=self.year_var,
                ).grid(row=1, column=2, padx=10, pady=5)

                self.month_var = tk.StringVar(value=calendar.month_name[now.month])
                tk.Label(self.root, text='Month').grid(row=1, column=3, padx=10, pady=5)
                ttk.Combobox(
                    self.root,
                    state="readonly",
                    values= list(calendar.month_name)[1:],
                    textvariable=self.month_var,
                ).grid(row=1, column=4, padx=10, pady=5)

                tk.Button(self.root, text='Refresh', command=refresh).grid(row=1, column=5, padx=5, pady=5)


            tk.Label(self.root, text="Select Employee:").grid(row=2, column=1, columnspan=5, padx=10, pady=10)

            for i, (user_id, user_name, user) in enumerate(self.employees):
                tk.Button(self.root,
                          text=f'{user_name} ({user_id})', 
                          command=lambda user=user: self.onselect(user))\
                    .grid(row=3+i, column=1, columnspan=2, padx=10, pady=10)
                
                if self.for_salary:
                    statuses[user_id] = tk.Label(self.root, text='100% Verified (0 Remaining)')
                    statuses[user_id].grid(row=3+i, column=3, columnspan=2, padx=10, pady=10)
            
            if self.for_salary: refresh()

    def get_overall_timesheet_status(self):
        year = self.year_var.get()
        month = self.month_var.get()
        month = [i for i, m in enumerate(calendar.month_name) if m == month][0]
        return select_query(f'select employee, avg(verified), count(*)-sum(verified) as avg ' + 
                            f'from timesheet where extract(year from event_time)={year} and ' + 
                            f'extract(month from event_time)={month} ' + 
                            f'group by employee')
            
    def onselect(self, employee):
        if self.for_salary:
            year = self.year_var.get()
            month = self.month_var.get()
            month = [i for i, m in enumerate(calendar.month_name) if m == month][0]

            TimesheetViewApp(tk.Toplevel(self.root), employee, year, month)
        else:
            TimesheetCreateApp(tk.Toplevel(self.root), employee)

    def fetch_employees(self):
        self.employees = []
        for emp in select_query('select * from employee_v1'):
            self.employees.append((emp[0], emp[7] + ' ' + emp[8], emp))

    