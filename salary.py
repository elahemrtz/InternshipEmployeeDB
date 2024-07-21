import tkinter as tk
from tkinter import *
from datetime import datetime
from database import query, select_query
import timesheet

class UserProfileApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Employee List")

        self.fetch_employees()

        self.create_widget()
        self.root.mainloop()

    def create_widget(self):
        if len(self.employees) == 0:
            tk.Label(self.root, text='No Employees available!').pack(padx=10, pady=10)
        else:
            tk.Label(self.root, text="Select Employee:").pack(padx=10, pady=10)

            for user_id, user_name, user in self.employees:
                tk.Button(self.root,
                          text=f'{user_name} ({user_id})', 
                          command=lambda user_id=user_id, user_name=user_name, user=user: self.open_profile(user_id, user_name, user))\
                    .pack(padx=10, pady=10)
            
    def fetch_employees(self):
        self.employees = []
        for emp in select_query('select * from employee_v1'):
            self.employees.append((emp[0], emp[7] + ' ' + emp[8], emp))

    
    def open_profile(self, user_id, user_name, user):
        profile_window = tk.Toplevel(self.root)
        profile_window.title(f"{user_name}'s Information")
        
        tk.Label(profile_window, text=f"Name: {user_name}")\
            .pack(padx=10, pady=20)

        # Additional profile information can be added here
        tk.Label(profile_window, text=f"Profile info:")\
            .pack(padx=10, pady=10)
        
        tk.Label(profile_window, text=f'SSID: {user[12]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(profile_window, text=f'Gender: {user[1]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(profile_window, text=f'Department: {user[2]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(profile_window, text=f'Marital Status: {user[3]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(profile_window, text=f'Position: {user[4]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(profile_window, text=f'Education: {user[6]} {user[5]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(profile_window, text=f'Date of Birth: {datetime.strftime(user[9], '%Y-%m-%d')}')\
            .pack(padx=10, pady=5)
        
        tk.Label(profile_window, text=f'Phone Number: {user[10]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(profile_window, text=f'Email Address: {user[11]}')\
            .pack(padx=10, pady=5)

        tk.Label(profile_window, text=f"Salary info:")\
            .pack(padx=10, pady=10)
    
        tk.Label(profile_window, 
                 text=f'Base Salary: {user[14]}'
                 if user[13] == 'Full-Time' 
                 else f'Minimum Hours per Week: {user[17]}')\
            .pack(padx=10, pady=5)
    
        tk.Label(profile_window, 
                 text=f'Weekly Hours: {user[15]}-{user[16]}'
                 if user[13] == 'Full-Time' 
                 else f'Hourly Wage: {user[18]}')\
            .pack(padx=10, pady=5)
        
        tk.Button(text='View Timesheet', command=lambda:self.go_to_timesheet(user_id))
        
    def calculate_salary(self):
        #calculate data for selected employee
        #emp sal info = [base , delay , overtime]
        id = self.selected_employee.get()
        select_query('select BASE_AMOUNT from employee where id = {id}')
        select_query('select OVERTIME_AMOUNT , DELAYS_AMOUNT from salary where EMPLOYEE = {id}')

    def open_timesheet(self, user_id):
        timesheet.TimesheetApp()

