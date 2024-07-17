from logging import root
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import database
from database import query


def show_employee_form():
    root=tk.Tk()
    root.title("Employee Form")

    tk.Label(root, text="First Name").grid(row=0, column=0)
    fname = tk.Entry(root)
    fname.grid(row=0, column=1, sticky='we' , pady=10)

    tk.Label(root, text="Last Name").grid(row=1, column=0)
    lname = tk.Entry(root)
    lname.grid(row=1, column=1, sticky='we', pady=10)

    tk.Label(root, text="SSID").grid(row=2, column=0)
    ssid = tk.Entry(root)
    ssid.grid(row=2, column=1, sticky='we', pady=10)

    tk.Label(root, text="Date of Birth").grid(row=3, column=0)
    dob = tk.Entry(root)
    dob.grid(row=3, column=1, sticky='we', pady=10)

    tk.Label(root, text="Marital Status").grid(row=4, column=0)
    marital_status = tk.StringVar()
    ttk.Combobox(
        state="readonly",
        values=list(database.constants['marital_status'].values()),
        textvariable=marital_status,
    ).grid(row=4, column=1, sticky='we', pady=10)

    tk.Label(root, text="Gender").grid(row=5, column=0)
    gender = tk.StringVar()
    ttk.Combobox(
        state="readonly",
        values=list(database.constants['gender'].values()),
        textvariable=gender,
    ).grid(row=5, column=1, sticky='we', pady=10)


    tk.Label(root, text="Position").grid(row=6, column=0)
    emp_position = tk.StringVar()
    ttk.Combobox(
        state="readonly",
        values=list(database.constants['emp_position'].values()),
        textvariable=emp_position,
    ).grid(row=6, column=1, sticky='we', pady=10)

    tk.Label(root, text="Department").grid(row=7, column=0)
    department = tk.StringVar()
    ttk.Combobox(
        state="readonly",
        values=list(database.constants['department'].values()),
        textvariable=department
    ).grid(row=7, column=1, sticky='we', pady=10)
    

    tk.Label(root, text="Edu Prog").grid(row=8, column=0)
    edu_prog = tk.StringVar()
    ttk.Combobox(
        state="readonly",
        values=list(database.constants['edu_prog'].values()),
        textvariable=edu_prog,
    ).grid(row=8, column=1, sticky='we', pady=10)


    tk.Label(root, text="Edu Level").grid(row=9, column=0)
    edu_level = tk.StringVar()
    ttk.Combobox(
        state="readonly",
        values=list(database.constants['edu_level'].values()),
        textvariable=edu_level,
    ).grid(row=9, column=1, sticky='we', pady=10)

    tk.Label(root, text="Address").grid(row=10, column=0)
    address = tk.Entry(root)
    address.grid(row=10, column=1, sticky='we', pady=10)

    tk.Label(root, text="Phone Number").grid(row=11, column=0)
    phone = tk.Entry(root)
    phone.grid(row=11, column=1, sticky='we', pady=10)

    tk.Label(root, text="Email Address").grid(row=12, column=0)
    email = tk.Entry(root)
    email.grid(row=12, column=1, sticky='we', pady=10)

    tk.Label(root, text="Employee Contract").grid(row=13, column=0)
    employee_type = tk.StringVar()
    ttk.Combobox(
        state="readonly",
        values= ['Full-Time' , 'Part-Time'],
        textvariable=employee_type,
    ).grid(row=13, column=1, sticky='we', pady=10)

    tk.Button(root, 
              text="Submit", 
              command=lambda: submit_data(
                  fname.get(),
                  lname.get(), 
                  ssid.get(), 
                  dob.get(), 
                  marital_status.get(),
                  gender.get(), 
                  emp_position.get(), 
                  department.get(), 
                  address.get(),
                  phone.get(), 
                  email.get(),
                  employee_type.get(),
                  )).grid(row=16, column=1)

    root.mainloop()

def submit_data(fname, lname, ssid, dob, marital_status, gender, position, department, address, phone, email, employee_type):
    print(f"First Name: {fname}")
    print(f"Last Name: {lname}")
    print(f"SSID: {ssid}")
    print(f"Date of Birth: {dob}")
    print(f"Marital Status: {marital_status}")
    print(f"Gender: {gender}")
    print(f"Position: {position}")
    print(f"Department: {department}")
    print(f"Address: {address}")
    print(f"Phone Number: {phone}")
    print(f"Email Address: {email}")
    print(f"Employee Type: {employee_type}")

    if fname == '' or lname == '' or ssid == '' or dob == '' or marital_status == '' or \
        gender == '' or position == '' or department == '' or address == '' or phone == '' or \
        email == '' or employee_type == '':
        return messagebox.showerror('Error!', 'All Fields are required!')

    marital_status = find_constant_key('marital_status', marital_status)
    gender = find_constant_key('gender', gender)
    position = find_constant_key('emp_position', position)
    department = find_constant_key('department', department)

    query(f'insert into employee (first_name, last_name, ssid, dob, marital_status, gender, position, department, address, phone_number, email_address, employee_type) values ' + 
          f'($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12)',
          [fname, lname, ssid, dob, marital_status, gender, position, department, address, phone, email, employee_type])

def find_constant_key(table_name, value):
    return [k for k, v in database.constants[table_name].items() if v == value][0]