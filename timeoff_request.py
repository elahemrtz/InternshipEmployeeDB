import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from database import select_query

class LeaveApplication:
    def __init__(self,root):
        self.root=root        
        self.root.title("Leave Request Form")
        self.fetch_employees()
        self.create_widgets()
    
    def fetch_employees(self):
        self.emp_names = {}
        for emp in select_query('select * from employee_v1'):
            self.emp_names[f'{emp[0]}'] = emp[7] + ' ' + emp[8]

    def create_widgets(self):
        tk.Label(self.root, text="Employee ID:").grid(row=0, column=0, padx=10, pady=10)
        self.emp_id_entry = tk.Entry(self.root)
        self.emp_id_entry.grid(row=0, column=1)

        self.search_button = tk.Button(self.root, text="Search", command=self.search_employee)
        self.search_button.grid(row=0, column=2)

        self.emp_name_label = tk.Label(self.root, text="")
        self.emp_name_label.grid(row=1, column=0, columnspan=3)

        tk.Label(self.root, text="Leave Type:").grid(row=2, column=0, padx=10, pady=10)
        self.leave_type = tk.StringVar(value="Daily")
        tk.Radiobutton(self.root, text="Daily", variable=self.leave_type, value="Daily", command=self.toggle_fields).grid(row=2, column=1, sticky=tk.W)
        tk.Radiobutton(self.root, text="Hourly", variable=self.leave_type, value="Hourly", command=self.toggle_fields).grid(row=2, column=2, sticky=tk.W)

        

        tk.Label(self.root, text="Start Date:").grid(row=4, column=0, padx=10, pady=10)
        self.start_date_entry = tk.Entry(self.root)
        self.start_date_entry.grid(row=4, column=1)

        tk.Label(self.root, text="End Date:").grid(row=5, column=0, padx=10, pady=10)
        self.end_date_entry = tk.Entry(self.root)
        self.end_date_entry.grid(row=5, column=1)

        

        tk.Label(self.root, text="Leave Date:").grid(row=3, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Start Time:").grid(row=6, column=0, padx=10, pady=10)
        self.start_time_entry = tk.Entry(self.root)
        self.start_time_entry.grid(row=6, column=1)

        tk.Label(self.root, text="End Time:").grid(row=7, column=0, padx=10, pady=10)
        self.end_time_entry = tk.Entry(self.root)
        self.end_time_entry.grid(row=7, column=1)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_request)
        self.submit_button.grid(row=8, column=0, columnspan=3, pady=20)

        self.toggle_fields()

    def toggle_fields(self):
        if self.leave_type.get() == "Daily":
            self.date_entry.configure(state='disabled')
            self.start_time_entry.configure(state='disabled')
            self.end_time_entry.configure(state='disabled')
            self.start_date_entry.configure(state='normal')
            self.end_date_entry.configure(state='normal')
        else:
            self.date_entry.configure(state='normal')
            self.start_time_entry.configure(state='normal')
            self.end_time_entry.configure(state='normal')
            self.start_date_entry.configure(state='disabled')
            self.end_date_entry.configure(state='disabled')

    def search_employee(self):
        emp_id = self.emp_id_entry.get()
        if emp_id in self.emp_names:
            self.emp_name_label.config(text=f"Employee Name: {self.emp_names[emp_id]}")
        else:
            self.emp_name_label.config(text="Employee not found")
    
    def submit_request(self):
        emp_id = self.emp_id_entry.get()
        leave_type = self.leave_type.get()

        if not emp_id:
            messagebox.showerror("Error", "Please enter the employee ID.")
            return

        if leave_type == "Daily":
            date = self.date_entry.get()

        if not date:
            messagebox.showerror("Error", "Please enter the leave date.")
            return

            try:
                date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Date should be in YYYY-MM-DD format.")
                return

                messagebox.showinfo("Success", "Your daily leave request has been submitted.")
        else:
            start_date = self.start_date_entry.get()
            end_date = self.end_date_entry.get()
            start_time = self.start_time_entry.get()
            end_time = self.end_time_entry.get()

        if not start_date or not end_date or not start_time or not end_time:
            messagebox.showerror("Error", "Please enter the start and end dates and times.")
            return

            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
                start_time = datetime.strptime(start_time, "%H:%M")
                end_time = datetime.strptime(end_time, "%H:%M")
            except ValueError:
                messagebox.showerror("Error", "Dates should be in YYYY-MM-DD format and times should be in HH:MM format.")
                return

        hours_diff = (end_time - start_time).seconds / 3600
        days_diff = (end_date - start_date).days + 1

        if hours_diff > 4:
            messagebox.showerror("Error", "You cannot take more than 4 hours of leave in a single day.")
        elif days_diff > 2.5:
            messagebox.showerror("Error", "You cannot take more than 2.5 days of leave.")
        else:
            messagebox.showinfo("Success", "Your hourly leave request has been submitted.")

if __name__ == "__main__":
    root=(tk.Tk())
    LeaveApplication(root)
    root.mainloop()


