import tkinter as tk
from tkinter import *
from datetime import datetime
from database import query
import database

class UserProfileApp:
    def _init_(self , root):
        self.root = root
        self.root.title("Employee List")

        #self.employees = []

        self.employees = [(2, 'lkmcl cmdslc'), (5, 'cdsdlkc dsmclds'), (7, ';lcdsmc ml,dcs;c')]

        self.selected_employee = tk.IntVar(value=self.employees[0][1]) if len(self.employees) > 0 else None

        self.create_widget()

    def create_widget(self):
        if len(self.employees) == 0:
            tk.Label(self.root, text='No Employees available!').grid(row=0, column=0, padx=10, pady=10)
        else:
            tk.Label(self.root, text="Select Employee:").grid(row=0, column=0, padx=10, pady=10)

            for idx, (idx2, name) in enumerate(self.employees):
                tk.Radiobutton(self.root, 
                               text=name, 
                               value=idx2, 
                               variable=self.selected_employee)\
                               .grid(row=idx+1, column=0, sticky='w', padx=10, pady=10)

            tk.Button(self.root, text="View Salary", command=self.open_profile)\
                .grid(row=len(self.employees)+2, column=0, padx=10, pady=10)

    def fetch_employees(self):
        self.employees = []
        for emp in query('select id, first_name, last_name from employee'):
            self.employees.append((emp[0], emp[1] + ' ' + emp[2]))

    
    def open_profile(self):
        user = self.selected_employee.get()
        # get employee base , overtime , delay
        base = 50
        delays = 20
        overtime = 30
        total = base + overtime - delays
        profile_window = tk.Toplevel(self.root)
        profile_window.title(f"{user}'s Salary")
        
        lbl_user_name = tk.Label(profile_window, text=f"Name: {user}")
        lbl_user_name.pack(padx=10, pady=10)

        # Additional profile information can be added here
        lbl_profile_info = tk.Label(profile_window, text=f"Salary info for {user} goes here.")
        lbl_profile_info.pack(padx=10, pady=10)   

        lbl_base = tk.Label(profile_window , text=f"Base Salary : {base}")
        lbl_base.pack(padx=10, pady=10)

        lbl_ot = tk.Label(profile_window , text=f"Overtime Amount : {overtime}")
        lbl_ot.pack(padx=10, pady=10)

        lbl_d = tk.Label(profile_window , text=f"Delay Amount : {delays}")
        lbl_d.pack(padx=10, pady=10)

        lbl_t = tk.Label(profile_window , text=f"Total Amount : {total}")
        lbl_t.pack(padx=10, pady=10)



    def calculate_salary(self):
        #calculate data for selected employee
        #emp sal info = [base , delay , overtime]
        id = self.selected_employee.get()
        query('select BASE_AMOUNT from employee where id = {id}')
        query('select OVERTIME_AMOUNT , DELAYS_AMOUNT from salary where EMPLOYEE = {id}')



if __name__ == "__main__":

#connect to database 
    database.connect_db()
#get list of employees 
    query('select * from gender')
    print(type(query))
#call function to compute total
    


    root = tk.Tk()
    app = UserProfileApp()
    app._init_(root=root)
    root.mainloop()    

