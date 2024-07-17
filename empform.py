from logging import root
import tkinter as tk
from tkinter import ttk

import database
from database import query

def show_employee_form():
    root=tk.Tk()
    root.title("Employee Form")

    tk.Label(root, text="First Name").grid(row=0, column=0)
    entry_fname = tk.Entry(root)
    entry_fname.grid(row=0, column=1)

    tk.Label(root, text="Last Name").grid(row=1, column=0)
    entry_lname = tk.Entry(root)
    entry_lname.grid(row=1, column=1)

    tk.Label(root, text="SSID").grid(row=2, column=0)
    entry_ssid = tk.Entry(root)
    entry_ssid.grid(row=2, column=1)

    tk.Label(root, text="Date of Birth (YYYY-MM-DD)").grid(row=3, column=0)
    entry_dob = tk.Entry(root)
    entry_dob.grid(row=3, column=1)

    tk.Label(root, text="Marital Status").grid(row=4, column=0)
    entry_marital_status = tk.Entry(root)
    entry_marital_status.grid(row=4, column=1)

    tk.Label(root, text="Gender").grid(row=5, column=0)
    ttk.Combobox(
        state="readonly",
        values=list(database.constants['gender'].values())
    ).grid(row=5, column=1)


    tk.Label(root, text="Position").grid(row=6, column=0)
    entry_position = tk.Entry(root)
    entry_position.grid(row=6, column=1)

    tk.Label(root, text="Department").grid(row=7, column=0)
    entry_department = tk.Entry(root)
    entry_department.grid(row=7, column=1)

    tk.Label(root, text="Address").grid(row=8, column=0)
    entry_address = tk.Entry(root)
    entry_address.grid(row=8, column=1)

    tk.Label(root, text="Phone Number").grid(row=9, column=0)
    entry_phone = tk.Entry(root)
    entry_phone.grid(row=9, column=1)

    tk.Label(root, text="Email Address").grid(row=10, column=0)
    entry_email = tk.Entry(root)
    entry_email.grid(row=10, column=1)

    tk.Button(root, text="Submit", command=lambda: submit_data(entry_fname.get(),
    entry_lname.get(), entry_ssid.get(), entry_dob.get(), entry_marital_status.get(),
    entry_gender.get(), entry_position.get(), entry_department.get(), entry_address.get(),
    entry_phone.get(), entry_email.get())).grid(row=11, column=1)

    root.mainloop()

def submit_data(fname, lname, ssid, dob, marital_status, gender, position, department, address, phone, email):
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

    query(f'insert into employee (first_name, last_name, ssid, dob, marital_)')
