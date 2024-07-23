import tkinter as tk
from tkinter import *
from datetime import datetime
from database import query, select_query
import timesheet

class UserProfileApp:
    def __init__(self, root, user_id, user_name, user):
        self.root = root or tk.Tk()
        self.root.title(f"{user_name}'s Information")
        
        self.user_id = user_id
        self.user_name = user_name
        self.user = user

        self.create_widget()
        self.root.mainloop()

    def create_widget(self):        
        tk.Label(self.root, text=f"Name: {self.user_name}")\
            .pack(padx=10, pady=20)

        # Additional profile information can be added here
        tk.Label(self.root, text=f"Profile info:")\
            .pack(padx=10, pady=10)
        
        tk.Label(self.root, text=f'SSID: {self.user[12]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(self.root, text=f'Gender: {self.user[1]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(self.root, text=f'Department: {self.user[2]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(self.root, text=f'Marital Status: {self.user[3]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(self.root, text=f'Position: {self.user[4]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(self.root, text=f'Education: {self.user[6]} {self.user[5]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(self.root, text=f'Date of Birth: {datetime.strftime(self.user[9], '%Y-%m-%d')}')\
            .pack(padx=10, pady=5)
        
        tk.Label(self.root, text=f'Phone Number: {self.user[10]}')\
            .pack(padx=10, pady=5)
        
        tk.Label(self.root, text=f'Email Address: {self.user[11]}')\
            .pack(padx=10, pady=5)

        tk.Label(self.root, text=f"Salary info:")\
            .pack(padx=10, pady=10)
    
        tk.Label(self.root, 
                 text=f'Base Salary: {self.user[14]}'
                 if self.user[13] == 'Full-Time' 
                 else f'Minimum Hours per Week: {self.user[17]}')\
            .pack(padx=10, pady=5)
    
        tk.Label(self.root, 
                 text=f'Weekly Hours: {self.user[15]}-{self.user[16]}'
                 if self.user[13] == 'Full-Time' 
                 else f'Hourly Wage: {self.user[18]}')\
            .pack(padx=10, pady=5)
        
        tk.Button(self.root, text='View Timesheet', command=lambda:self.open_timesheet(self.user))\
            .pack(padx=10, pady=10)
        
    def calculate_salary(self):
        #calculate data for selected employee
        id = self.selected_employee.get()
        select_query('select BASE_AMOUNT from employee where id = {id}')
        select_query('select OVERTIME_AMOUNT , DELAYS_AMOUNT from salary where EMPLOYEE = {id}')

    def open_timesheet(self, user_id):
        timesheet.TimesheetApp(tk.Toplevel(self.root), user_id, as_manager=True)