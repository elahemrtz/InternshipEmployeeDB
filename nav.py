import tkinter as tk
from empform import *
from timesheet import *
from employee_select import *
from timeoff_request import *

class NavApp:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('سیستم اداری')
        self.create_widget()
    
    def create_widget(self):
        tk.Button(self.root, text='Employee Form', command=self.employee_form_nav)\
            .pack(padx=10, pady=10)
        tk.Button(self.root, text='Timesheet Create Form', command=self.timesheet_create_nav)\
            .pack(padx=10, pady=10)
        tk.Button(self.root, text='Timesheet View Form', command=self.timesheet_view_nav)\
            .pack(padx=10, pady=10)
        tk.Button(self.root, text='Timeoff Request Form', command=self.timeoff_request_nav)\
            .pack(padx=10, pady=10)
    
    def employee_form_nav(self):
        EmployeeForm(tk.Toplevel(self.root))
    
    def timesheet_create_nav(self):
        EmployeeSelectApp(tk.Toplevel(self.root),
                          onselect=lambda user: TimesheetCreateApp(tk.Toplevel(self.root), user))

    def timesheet_view_nav(self):
        EmployeeSelectApp(tk.Toplevel(self.root),
                          onselect=lambda user: TimesheetViewApp(tk.Toplevel(self.root), user))

    def timeoff_request_nav(self):
        LeaveApplication(tk.Toplevel(self.root))