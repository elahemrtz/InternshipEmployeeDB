
import tkinter as tk
from datetime import datetime
from tkinter import ttk
from database import query, select_query
import database
import calendar

class TimesheetApp:
    def __init__(self, root, employee, as_manager=False):
        self.root = root or tk.Tk()
        self.root.title(f"{employee[7]} {employee[9]}\'s Timesheet")

        self.employee = employee
        self.as_manager = as_manager
        self.timesheet_views = []

        self.create_widgets()
        self.root.mainloop()

    def fetch_employees(self):
        self.employees = []
        for emp in select_query('select id, first_name, last_name from employee'):
            self.employees.append((emp[0], emp[1] + ' ' + emp[2]))

    def create_widgets(self):
        if self.as_manager:
            now = datetime.now()
            year_var = tk.IntVar(value=now.year)
            tk.Label(self.root, text='Year').grid(row=1, column=1, padx=10, pady=5)
            ttk.Combobox(
                self.root,
                state="readonly",
                values= list(range(now.year-10, now.year+1))[::-1],
                textvariable=year_var,
            ).grid(row=1, column=2, padx=10, pady=5)

            month_var = tk.StringVar(value=calendar.month_name[now.month])
            tk.Label(self.root, text='Month').grid(row=1, column=3, padx=10, pady=5)
            ttk.Combobox(
                self.root,
                state="readonly",
                values= list(calendar.month_name)[1:],
                textvariable=month_var,
            ).grid(row=1, column=4, padx=10, pady=5)

            tk.Button(self.root,
                      text='View Month Timesheet', 
                      command=lambda: self.display_timesheet(year_var.get(), month_var.get())
            ).grid(row=1, column=5, padx=10, pady=10)
        else:
            tk.Button(self.root, text="Clock In", command=self.enter).pack(padx=10, pady=10)
            tk.Button(self.root, text="Clock Out", command=self.exit).pack(padx=10, pady=10)

    def display_timesheet(self, year: int, month: str):
        month = [i for i, m in enumerate(calendar.month_name) if m == month][0]
        for v in self.timesheet_views:
            v.grid_forget()
        self.timesheet_views = []

        for i, (event_type, event_time, verified) in enumerate(self.fetch_timesheet(year, month)):
            event_time = event_time.strftime('%Y-%m-%d %H:%M:%S')

            if i == 0:
                self.timesheet_views += [tk.Label(self.root, text='Verified')]
                self.timesheet_views[-1].grid(row=2, column=1, padx=10, pady=10)

                self.timesheet_views += [tk.Label(self.root, text='Type')]
                self.timesheet_views[-1].grid(row=2, column=2, padx=10, pady=10)

                self.timesheet_views += [tk.Label(self.root, text='Time')]
                self.timesheet_views[-1].grid(row=2, column=3, padx=10, pady=10)

            self.timesheet_views += [tk.Checkbutton(self.root, variable=tk.BooleanVar(value=verified == 1))]
            self.timesheet_views[-1].grid(row=3+i, column=1, padx=10, pady=10)

            self.timesheet_views += [tk.Label(self.root, text=event_type)]
            self.timesheet_views[-1].grid(row=3+i, column=2, padx=10, pady=10)

            self.timesheet_views += [tk.Label(self.root, text=event_time)]
            self.timesheet_views[-1].grid(row=3+i, column=3, padx=10, pady=10)

    def fetch_timesheet(self, year, month):
        return select_query(f'select tt.name, t.event_time, t.verified from timesheet t left join timesheet_type tt on t.event_type=tt.id where t.employee={self.employee[0]} and extract(year from t.event_time)={year} and extract(month from t.event_time)={month}')

    def enter(self):
        self.save_time(self.employee, 'Enter')

    def exit(self):
        self.save_time(self.employee, 'Exit')

    def save_time(self, employee, action):
        action = self.find_constant_key('timesheet_type', action)
        time = datetime.now().strftime('%Y-%m-$d %H:%M:%S.%Z')
        query(f"insert into timesheet (event_type, event_time, employee) values " +
              f"({action}, to_timestamp('{time}', 'YYYY-MM-DD HH:MI:SS.FF'), {employee[0]})")    

    def find_constant_key(self, table_name, value):
        return [k for k, v in database.constants[table_name].items() if v == value][0]
