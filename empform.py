
from datetime import datetime
import re
import tkinter as tk
from tkinter import  ttk
from tkinter import messagebox
from typing import Optional

 


import database
from database import find_constant_key, query, select_query

class EmployeeForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Form")
        #self.frame = Frame(root)
        self.create_widget()



    def create_widget(self):
        #Toplevel.geometry("700x350")

        tk.Label(self.root, text="First Name").grid(row=0, column=0)
        fname = tk.Entry(self.root)
        fname.grid(row=0, column=1, sticky='we' , pady=10)

        tk.Label(self.root, text="Last Name").grid(row=0, column=2)
        lname = tk.Entry(self.root)
        lname.grid(row=0, column=3, sticky='we', pady=10)

        tk.Label(self.root, text="SSID").grid(row=1, column=0)
        ssid = tk.Entry(self.root)
        ssid.grid(row=1, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Date of Birth").grid(row=1, column=2)
        dob = tk.Entry(self.root)
        dob.grid(row=1, column=3, sticky='we', pady=10)

        tk.Label(self.root, text="Marital Status").grid(row=2, column=0)
        marital_status = tk.StringVar()
        ttk.Combobox(
            self.root,
            state="readonly",
            values=list(database.constants['marital_status'].values()),
            textvariable=marital_status,
        ).grid(row=2, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Gender").grid(row=2, column=2)
        gender = tk.StringVar()
        ttk.Combobox(
            self.root,
            state="readonly",
            values=list(database.constants['gender'].values()),
            textvariable=gender,
        ).grid(row=2, column=3, sticky='we', pady=10)


        tk.Label(self.root, text="Position").grid(row=3, column=0)
        emp_position = tk.StringVar()
        ttk.Combobox(
            self.root,
            state="readonly",
            values=list(database.constants['emp_position'].values()),
            textvariable=emp_position,
        ).grid(row=3, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Department").grid(row=3, column=2)
        department = tk.StringVar()
        ttk.Combobox(
            self.root,
            state="readonly",
            values=list(database.constants['department'].values()),
            textvariable=department
        ).grid(row=3, column=3, sticky='we', pady=10)
        

        tk.Label(self.root, text="Edu Prog").grid(row=4, column=0)
        edu_prog = tk.StringVar()
        ttk.Combobox(
            self.root,
            state="readonly",
            values=list(database.constants['edu_prog'].values()),
            textvariable=edu_prog,
        ).grid(row=4, column=1, sticky='we', pady=10)


        tk.Label(self.root, text="Edu Level").grid(row=4, column=2)
        edu_level = tk.StringVar()
        ttk.Combobox(
            self.root,
            state="readonly",
            values=list(database.constants['edu_level'].values()),
            textvariable=edu_level,
        ).grid(row=4, column=3, sticky='we', pady=10)

        tk.Label(self.root, text="Address").grid(row=5, column=0)
        address = tk.Entry(self.root)
        address.grid(row=5, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Phone Number").grid(row=5, column=2)
        phone = tk.Entry(self.root)
        phone.grid(row=5, column=3, sticky='we', pady=10)

        tk.Label(self.root, text="Email Address").grid(row=6, column=0)
        email = tk.Entry(self.root)
        email.grid(row=6, column=1, sticky='we', pady=10)

        tk.Label(self.root, text="Employee Contract").grid(row=6, column=2)
        employee_type = tk.StringVar()

        #base_salary =  tk.Label(self.root, text="Base Salary"), tk.Entry(self.root)
        min_weekly_hour = tk.Label(self.root, text="Minimum Monthly Hours"), tk.Entry(self.root)
        hourly_wage = tk.Label(self.root, text="Hourly Wage"), tk.Entry(self.root)

        def option_selected(_):
            if employee_type.get() == 'Full-Time':
                min_weekly_hour[0].grid_forget()
                min_weekly_hour[1].grid_forget()
                #hourly_wage[0].grid_forget()
               # hourly_wage[1].grid_forget()


                hourly_wage[0].grid(row=7, column=0)
                hourly_wage[1].grid(row=7, column=1, sticky='we', pady=10)

               # base_salary[0].grid(row=7, column=0)
               # base_salary[1].grid(row=7, column=1, sticky='we', pady=10)
            else:
                # base_salary[0].grid_forget()
               # base_salary[1].grid_forget()

                min_weekly_hour[0].grid(row=7, column=2)
                min_weekly_hour[1].grid(row=7, column=3, sticky='we', pady=10)

                hourly_wage[0].grid(row=7, column=0)
                hourly_wage[1].grid(row=7, column=1, sticky='we', pady=10)


        cbox = ttk.Combobox(
            self.root,
            state="readonly",
            values= ['Full-Time' , 'Part-Time'],
            textvariable=employee_type,
        )
        cbox.grid(row=6, column=3, sticky='we', pady=10)
        cbox.bind("<<ComboboxSelected>>", option_selected)

        tk.Button(self.root, 
                text="Submit", 
                command=lambda: self.submit_data(fname.get(), lname.get(),  ssid.get(),  dob.get(),  marital_status.get(), 
                                                 gender.get(),  emp_position.get(),  department.get(),  address.get(), phone.get(),  
                                                 email.get(), edu_prog.get(), edu_level.get(), employee_type.get(), 
                                                 min_weekly_hour[1].get(), hourly_wage[1].get())
                ).grid(row=8, column=3)
        

       
        self.root.mainloop()

    def submit_data(self, fname, lname, ssid, dob, marital_status, gender, position, department, address, phone, email, 
                    edu_prog, edu_level, employee_type,min_weekly_hour,hourly_wage):
        
        if fname == '' or lname == '' or ssid == '' or dob == '' or marital_status == '' or \
            gender == '' or position == '' or department == '' or address == '' or phone == '' or \
            email == '' or edu_level == '' or edu_prog == '' or employee_type == '' or hourly_wage == '' or \
            (employee_type == 'Part-Time' and min_weekly_hour == ''):
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
        edu_prog = find_constant_key('edu_prog', edu_prog)
        edu_level = find_constant_key('edu_level', edu_level)
        try:
            datetime.strptime(dob, '%Y-%m-%d')

        except:
            return messagebox.showerror('Error!', 'Format of Date of Birth should be YYYY-MM-dd!')
        
        if employee_type != 'Full-Time':
            try:
                min_weekly_hour = int(min_weekly_hour)
            except:
                return messagebox.showerror('Error!', 'Min Weekly Hours should be an integer!')
        try:
            hourly_wage = int(hourly_wage)
        except:
            return messagebox.showerror('Error!', 'Hourly Wage should be an integer!')
        
        keys_ = 'first_name, last_name, ssid, dob, marital_status, gender, position, department, address, phone_number, email_address, edu_prog, edu_level, employee_type, salary_per_hour'
        values_ = [fname, lname, ssid, f'to_date(\'{dob}\', \'YYYY-MM-DD\')', marital_status, gender, position, department, address, phone, email, edu_prog, edu_level, employee_type, hourly_wage]
        if employee_type == 'Full-Time': 
            keys_ += ', daily_start_time, daily_end_time'
            values_ += [9, 17]
        else: 
            keys_ += ', min_hour_per_month'
            values_ += [min_weekly_hour]

        for i in range(len(values_)):
            if isinstance(values_[i], str) and 'to_date' not in values_[i]: 
                values_[i] = f'\'{values_[i]}\''
            else:
                values_[i] = f'{values_[i]}'
        query(f'insert into employee ({keys_}) values ({', '.join(values_)})')
