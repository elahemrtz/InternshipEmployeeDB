import database
import empform
import timesheet
import salary
import employee_select
import tkinter as tk


database.connect_db()
database.initialize_constants()

employee_select.EmployeeSelectApp(
    onselect=lambda user_id, user_name, user, root: timesheet.TimesheetCreateApp(tk.Toplevel(root), user)
    )
# empform.EmployeeForm()
# salary.UserProfileApp()
