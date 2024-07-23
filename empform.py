from datetime import datetime
import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from typing import Optional

import database
from database import find_constant_key, query, select_query

class EmployeeForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Form")

        self.create_widget()
        self.root.mainloop()

    def create_widget(self):
        tk.Label(self.root, text="First Name").grid(row=0, column=0)
        fname = tk.Entry(self.root)
        fname.grid(row=0, column=1, sticky='we' , pady=10)

        tk.Label(self.root, text="Last Name").grid(row=1, column=0)
        lname = tk.Entry(self.root)
        lname.grid(row=1, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="SSID").grid(row=2, column=0)
        ssid = tk.Entry(self.root)
        ssid.grid(row=2, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Date of Birth").grid(row=3, column=0)
        dob = tk.Entry(self.root)
        dob.grid(row=3, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Marital Status").grid(row=4, column=0)
        marital_status = tk.StringVar()
        ttk.Combobox(
            state="readonly",
            values=list(database.constants['marital_status'].values()),
            textvariable=marital_status,
        ).grid(row=4, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Gender").grid(row=5, column=0)
        gender = tk.StringVar()
        ttk.Combobox(
            state="readonly",
            values=list(database.constants['gender'].values()),
            textvariable=gender,
        ).grid(row=5, column=1, sticky='we', pady=10)


        tk.Label(self.root, text="Position").grid(row=6, column=0)
        emp_position = tk.StringVar()
        ttk.Combobox(
            state="readonly",
            values=list(database.constants['emp_position'].values()),
            textvariable=emp_position,
        ).grid(row=6, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Department").grid(row=7, column=0)
        department = tk.StringVar()
        ttk.Combobox(
            state="readonly",
            values=list(database.constants['department'].values()),
            textvariable=department
        ).grid(row=7, column=1, sticky='we', pady=10)
        

        tk.Label(self.root, text="Edu Prog").grid(row=8, column=0)
        edu_prog = tk.StringVar()
        ttk.Combobox(
            state="readonly",
            values=list(database.constants['edu_prog'].values()),
            textvariable=edu_prog,
        ).grid(row=8, column=1, sticky='we', pady=10)


        tk.Label(self.root, text="Edu Level").grid(row=9, column=0)
        edu_level = tk.StringVar()
        ttk.Combobox(
            state="readonly",
            values=list(database.constants['edu_level'].values()),
            textvariable=edu_level,
        ).grid(row=9, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Address").grid(row=10, column=0)
        address = tk.Entry(self.root)
        address.grid(row=10, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Phone Number").grid(row=11, column=0)
        phone = tk.Entry(self.root)
        phone.grid(row=11, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Email Address").grid(row=12, column=0)
        email = tk.Entry(self.root)
        email.grid(row=12, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Employee Contract").grid(row=13, column=0)
        employee_type = tk.StringVar()

        base_salary =  tk.Label(self.root, text="Base Salary"), tk.Entry(self.root)
        min_weekly_hour = tk.Label(self.root, text="Minimum Weekly Hours"), tk.Entry(self.root)
        hourly_wage = tk.Label(self.root, text="Hourly Wage"), tk.Entry(self.root)

        def option_selected(_):
            if employee_type.get() == 'Full-Time':
                min_weekly_hour[0].grid_forget()
                min_weekly_hour[1].grid_forget()
                hourly_wage[0].grid_forget()
                hourly_wage[1].grid_forget()

                base_salary[0].grid(row=14, column=0)
                base_salary[1].grid(row=14, column=1, sticky='we', pady=10)
            else:
                base_salary[0].grid_forget()
                base_salary[1].grid_forget()

                min_weekly_hour[0].grid(row=14, column=0)
                min_weekly_hour[1].grid(row=14, column=1, sticky='we', pady=10)

                hourly_wage[0].grid(row=15, column=0)
                hourly_wage[1].grid(row=15, column=1, sticky='we', pady=10)


        cbox = ttk.Combobox(
            state="readonly",
            values= ['Full-Time' , 'Part-Time'],
            textvariable=employee_type,
        )
        cbox.grid(row=13, column=1, sticky='we', pady=10)
        cbox.bind("<<ComboboxSelected>>", option_selected)

        tk.Button(self.root, 
                text="Submit", 
                command=lambda: self.submit_data(fname.get(), lname.get(),  ssid.get(),  dob.get(),  marital_status.get(), gender.get(),  emp_position.get(),  department.get(),  address.get(), phone.get(),  email.get(), employee_type.get(), base_salary[1].get(), min_weekly_hour[1].get(), hourly_wage[1].get())
                ).grid(row=17, column=1)

        self.root.mainloop()

    def submit_data(self, fname, lname, ssid, dob, marital_status, gender, position, department, address, phone, email, employee_type,base_salary,min_weekly_hour,hourly_wage):
        
        if fname == '' or lname == '' or ssid == '' or dob == '' or marital_status == '' or \
            gender == '' or position == '' or department == '' or address == '' or phone == '' or \
            email == '' or employee_type == '' or \
            (employee_type == 'Full-Time' and base_salary == '' or employee_type == 'Part-Time' and min_weekly_hour + hourly_wage == ''):
            return messagebox.showerror('Error!', 'All Fields are required!')
        
        if len(select_query(f'select * from employee where ssid=\'{ssid}\'')) > 0:
            return messagebox.showerror('Error!', 'SSID should be unique!')
        
        if not re.compile(r'^[0-9]{10}$').match(ssid):
            return messagebox.showerror('Error!', 'Incorrect SSID format!')
        
        if not re.compile(r'^[0-9]{11}$').match(phone):
            return messagebox.showerror('Error!', 'Incorrect Phone number format!')
        
        if not re.compile('^.+@.+\\..+$').match(email):
            return messagebox.showerror('Error!', 'Incorrect Email format!')

        marital_status = find_constant_key('marital_status', marital_status)
        gender = find_constant_key('gender', gender)
        position = find_constant_key('emp_position', position)
        department = find_constant_key('department', department)
        try:
            datetime.strptime(dob, '%Y-%m-%d')
        except:
            return messagebox.showerror('Error!', 'Format of Date of Birth should be YYYY-MM-dd!')
        
        if employee_type == 'Full-Time':
            try:
                base_salary = int(base_salary)
            except:
                return messagebox.showerror('Error!', 'Base Salary should be an integer!')
        else:
            try:
                min_weekly_hour = int(min_weekly_hour)
            except:
                return messagebox.showerror('Error!', 'Min Weekly Hours should be an integer!')
            try:
                hourly_wage = int(hourly_wage)
            except:
                return messagebox.showerror('Error!', 'Hourly Wage should be an integer!')
        
        keys_ = 'first_name, last_name, ssid, dob, marital_status, gender, position, department, address, phone_number, email_address, employee_type'
        values_ = [fname, lname, ssid, f'to_date(\'{dob}\', \'YYYY-MM-DD\')', marital_status, gender, position, department, address, phone, email, employee_type]
        if employee_type == 'Full-Time': 
            keys_ += ', base_salary, daily_start_time, daily_end_time'
            values_ += [base_salary, 9, 17]
        else: 
            keys_ += ', min_hour_per_week, salary_per_hour'
            values_ += [min_weekly_hour, hourly_wage]

        for i in range(len(values_)):
            if isinstance(values_[i], str) and 'to_date' not in values_[i]: 
                values_[i] = f'\'{values_[i]}\''
            else:
                values_[i] = f'{values_[i]}'
        query(f'insert into employee ({keys_}) values ({', '.join(values_)})')
