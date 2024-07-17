
from ast import main
from logging import root
import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime
from database import query

class TimesheetApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Employee Timesheet")

        self.employees = []
        self.fetch_employees()
        self.selected_employee = tk.StringVar(value=self.employees[0]) if len(self.employees) > 0 else None

        self.create_widgets()
        self.root.mainloop()

    def fetch_employees(self):
        self.employees = []
        for emp in query('select id, first_name, last_name from employee'):
            self.employees.append((emp[0], emp[1] + ' ' + emp[2]))

    def create_widgets(self):
        if len(self.employees) == 0:
            tk.Label(self.root, text='No Employees available!').grid(row=0, column=0, padx=10, pady=10)
        else:
            tk.Label(self.root, text="Select Employee:").grid(row=0, column=0, padx=10, pady=10)

            tk.OptionMenu(self.root, self.selected_employee, *self.employees)\
                .grid(row=0, column=1, padx=10, pady=10)

            tk.Button(self.root, text="Clock In", command=self.clock_in)\
                .grid(row=1, column=0, padx=10, pady=10)

            tk.Button(self.root, text="Clock Out", command=self.clock_out)\
                .grid(row=1, column=1, padx=10, pady=10)

    def clock_in(self):
        employee = self.selected_employee.get()
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_time(employee, "Clock In", time)
        messagebox.showinfo("Success", f"{employee} clocked in at {time}.")

    def clock_out(self):
        employee = self.selected_employee.get()
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_time(employee, "Clock Out", time)
        messagebox.showinfo("Success", f"{employee} clocked out at {time}.")

    def save_time(self, employee, action, time):
        try:
            with open("timesheet.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([employee, action, time])
        except Exception as e:
            messagebox.showerror("Error", f"Could not save the time: {e}")
            

