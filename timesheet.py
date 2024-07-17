
from ast import main
from logging import root
import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

class TimesheetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Timesheet")

        self.employees = ["Alice", "Bob", "Charlie", "David", "Eve"]
        self.selected_employee = tk.StringVar(value=self.employees[0])

        self.create_widgets()

def create_widgets(self):
    tk.Label(self.root, text="Select Employee:").grid(row=0, column=0, padx=10, pady=10)

    self.employee_menu = tk.OptionMenu(self.root, self.selected_employee, *self.employees)
    self.employee_menu.grid(row=0, column=1, padx=10, pady=10)

    self.btn_clock_in = tk.Button(self.root, text="Clock In", command=self.clock_in)
    self.btn_clock_in.grid(row=1, column=0, padx=10, pady=10)

    self.btn_clock_out = tk.Button(self.root, text="Clock Out", command=self.clock_out)
    self.btn_clock_out.grid(row=1, column=1, padx=10, pady=10)

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
         
if __name__=="__main__": 
    main() 

