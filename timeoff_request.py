import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

from database import query, select_query

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
        leave_type =  self.leave_type.get()

        if not emp_id:
            messagebox.showerror('Error!', 'Employee ID is required!')
            return
        
        if leave_type == 'Hourly':
            date = self.date_entry.get()
            start_time = self.start_time_entry.get()
            end_time = self.end_time_entry.get()

            if not date:
                messagebox.showerror('Error!', 'Leave date is required!')
                return
            if not start_time:
                messagebox.showerror('Error!', 'Start time is required!')
                return
            if not end_time:
                messagebox.showerror('Error!', 'End time is required!')
                return
            
            try:
                datetime.strptime(date, '%Y-%m-%d')
            except:
                messagebox.showerror('Error!', 'Leave date format must be YYYY-MM-DD')
                return
            try:
                datetime.strptime(start_time, '%H:%M')
            except:
                messagebox.showerror('Error!', 'Start time format must be HH:MM')
                return
            try:
                datetime.strptime(end_time, '%H:%M')
            except:
                messagebox.showerror('Error!', 'End time format must be HH:MM')
                return
            
            start_time = datetime.strptime(f'{date} {start_time}:00', '%Y-%m-%d %H:%M:%S')
            end_time = datetime.strptime(f'{date} {end_time}:00', '%Y-%m-%d %H:%M:%S')
            hours = (end_time - start_time).seconds / 3600
            total_hours = self.get_employee_taken_hours(emp_id, start_time) + hours
            
            if hours > 4:
                messagebox.showerror('Error!', 'Hourly timeoff can be at most 4 hours')
                return
        
            if total_hours > 20:
                messagebox.showerror('Error!', 'The total timeoff is 20 hours per month')
                return
            
            start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')
            end_time = datetime.strftime(end_time, '%Y-%m-%d %H:%M:%S')
        else:
            start_date = self.start_date_entry.get()
            end_date = self.end_date_entry.get()

            if not start_date:
                messagebox.showerror('Error!', 'Start Date is required!')
                return
            if not end_date:
                messagebox.showerror('Error!', 'End Date is required!')
                return

            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
            except:
                messagebox.showerror('Error!', 'Leave date format must be YYYY-MM-DD')
                return
            try:
                end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
            except:
                messagebox.showerror('Error!', 'Leave date format must be YYYY-MM-DD')
                return
            
            if start_date.month == (end_date - timedelta(days=1)).month:
                hours = 8 * (end_date - start_date).days
                total_hours = self.get_employee_taken_hours(emp_id, start_date) + hours

                if total_hours > 20:
                    messagebox.showerror('Error!', 'The total timeoff is 20 hours per month')
                    return
            else:
                month_start = start_date + timedelta(days=1)
                while month_start.month == start_date.month: month_start += timedelta(days=1)

                hours1 = 8 * (month_start - start_date).days
                hours2 = 8 * (end_date - month_start).days
                total_hours1 = self.get_employee_taken_hours(emp_id, start_date) + hours1
                total_hours2 = self.get_employee_taken_hours(emp_id, end_date) + hours2

                if total_hours1 > 20 or total_hours2 > 20:
                    messagebox.showerror('Error!', 'The total timeoff is 20 hours per month')
                    return

                query(f'insert into timeoff (employee, type, start_time, end_time) values ' + 
                        f'({emp_id}, \'{leave_type}\', ' + 
                        f'to_date(\'{datetime.strftime(start_date, '%Y-%m-%d %H:%M:%S')}\', \'YYYY-MM-DD HH24:MI:SS\'), ' + 
                        f'to_date(\'{datetime.strftime(month_start, '%Y-%m-%d %H:%M:%S')}\', \'YYYY-MM-DD HH24:MI:SS\'))')
                start_date = month_start

            start_time = datetime.strftime(start_date, '%Y-%m-%d %H:%M:%S')
            end_time = datetime.strftime(end_date, '%Y-%m-%d %H:%M:%S')

        query(f'insert into timeoff (employee, type, start_time, end_time) values ' + 
                f'({emp_id}, \'{leave_type}\', ' + 
                f'to_date(\'{start_time}\', \'YYYY-MM-DD HH24:MI:SS\'), ' + 
                f'to_date(\'{end_time}\', \'YYYY-MM-DD HH24:MI:SS\'))')

    def get_employee_taken_hours(self, employee, date): 
        result = select_query(f'select sum(hours) from timeoff ' + 
                              f'where employee={employee} and ' + 
                              f'extract(month from start_time)={date.month} ' + 
                              f'and extract(year from start_time)={date.year}')
        return result[0][0] or 0

if __name__ == "__main__":
    root=(tk.Tk())
    LeaveApplication(root)
    root.mainloop()


