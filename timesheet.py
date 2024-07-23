
import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
from typing import Any, Dict, List
from database import find_constant_key, query, select_query
import database
import calendar

class TimesheetViewApp:
    def __init__(self, root, employee):
        self.root = root or tk.Tk()
        self.root.title(f"{employee[7]} {employee[8]}\'s Timesheet")

        self.employee = employee
        self.timesheet_views = []

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
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
                    text='Refresh Timesheet', 
                    command=lambda: self.display_timesheet(year_var.get(), month_var.get())
        ).grid(row=1, column=5, padx=10, pady=10)

    def display_timesheet(self, year: int, month: str):
        month = [i for i, m in enumerate(calendar.month_name) if m == month][0]
        for v in self.timesheet_views:
            v.grid_forget()
        self.timesheet_views = []

        timesheet = self.fetch_timesheet(year, month)
        for i, (idx, event_type, event_time, verified) in enumerate(timesheet):
            event_time = event_time.strftime('%Y-%m-%d %H:%M:%S')

            if i == 0:
                self.timesheet_views += [tk.Label(self.root, text='Verified')]
                self.timesheet_views[-1].grid(row=2, column=1, padx=10, pady=10)

                self.timesheet_views += [tk.Label(self.root, text='Type')]
                self.timesheet_views[-1].grid(row=2, column=2, padx=10, pady=10)

                self.timesheet_views += [tk.Label(self.root, text='Time')]
                self.timesheet_views[-1].grid(row=2, column=3, padx=10, pady=10)

                self.timesheet_views += [tk.Label(self.root, text='Deleted')]
                self.timesheet_views[-1].grid(row=2, column=4, padx=10, pady=10)

            self.timesheet_views += [tk.Checkbutton(self.root, 
                                                    variable=tk.IntVar(self.root, name=f'{idx}_verified', value=verified))]
            if verified: self.timesheet_views[-1].select()
            else: self.timesheet_views[-1].deselect()
            self.timesheet_views[-1].grid(row=3+i, column=1, padx=10, pady=10)

            self.timesheet_views += [ttk.Combobox(self.root, 
                                                 state="readonly",
                                                 values=['Enter', 'Exit'],
                                                 textvariable=tk.StringVar(self.root,
                                                                           name=f'{idx}_type',
                                                                           value=event_type))]
            self.timesheet_views[-1].current(['Enter', 'Exit'].index(event_type))
            self.timesheet_views[-1].grid(row=3+i, column=2, padx=10, pady=10)

            self.timesheet_views += [tk.Entry(self.root, 
                                              textvariable=tk.StringVar(self.root,
                                                                        name=f'{idx}_time',
                                                                        value=event_time))]
            self.timesheet_views[-1].grid(row=3+i, column=3, padx=10, pady=10)

            self.timesheet_views += [tk.Checkbutton(self.root, 
                                                    variable=tk.IntVar(self.root, name=f'{idx}_deleted', value=0))]
            self.timesheet_views[-1].grid(row=3+i, column=4, padx=10, pady=10)

        if len(timesheet):
            self.timesheet_views += [tk.Button(self.root, text='Save Changes', command=lambda timesheet=timesheet: self.save_changes(timesheet))]
            self.timesheet_views[-1].grid(row=3+len(timesheet), column=5, padx=10, pady=10)

    def fetch_timesheet(self, year, month):
        return select_query('select t.id, tt.name, t.event_time, t.verified ' + 
                            'from timesheet t left join timesheet_type tt on t.event_type=tt.id ' + 
                            f'where t.employee={self.employee[0]} and ' + 
                            f'extract(year from t.event_time)={year} ' + 
                            f'and extract(month from t.event_time)={month} ' + 
                            'order by t.event_time')

    def save_changes(self, timesheet):
        for idx, oevent_type, oevent_time, overified in timesheet:
            try:
                deleted = self.root.getvar(f'{idx}_deleted')
            except:
                deleted = 0
            try:
                verified = self.root.getvar(f'{idx}_verified')
            except:
                verified = overified
            try:
                event_type = self.root.getvar(f'{idx}_type')
            except:
                event_type = oevent_type
            try:
                event_time = self.root.getvar(f'{idx}_time')
            except:
                event_time = oevent_time.strftime('%Y-%m-%d %H:%M:%S')

            if deleted == 1:
                query(f'delete from timesheet where id={idx}')
                continue
            try: 
                datetime.strptime(event_time, '%Y-%m-%d %H:%M:%S')
            except:
                print(event_time)
                messagebox.showerror('Error!', 'Invalid timestamp format')
                break

            query(f"update timesheet set verified={verified}, event_type={1 if event_type == 'Enter' else 2}, event_time=to_timestamp('{event_time}', 'YYYY-MM-DD HH24:MI:SS.FF') where id={idx}")
    

class TimesheetCreateApp:
    def __init__(self, root, employee):
        self.root = root or tk.Tk()
        self.root.title(f"{employee[7]} {employee[8]}\'s Timesheet")

        self.employee = employee
        
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        tk.Label(self.root, text=f"{self.employee[7]} {self.employee[8]} ({self.employee[0]})").pack(padx=10, pady=10)
        tk.Button(self.root, text="Clock In", command=self.enter).pack(padx=10, pady=10)
        tk.Button(self.root, text="Clock Out", command=self.exit).pack(padx=10, pady=10)

    def enter(self):
        self.save_time(self.employee, 'Enter')

    def exit(self):
        self.save_time(self.employee, 'Exit')

    def save_time(self, employee, action):
        action = find_constant_key('timesheet_type', action)
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query(f"insert into timesheet (event_type, event_time, employee) values " +
              f"({action}, to_timestamp('{time}', 'YYYY-MM-DD HH24:MI:SS.FF'), {employee[0]})")

