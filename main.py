import database
import empform
import timesheet


database.connect_db()
database.initialize_constants()

timesheet.TimesheetApp()
empform.show_employee_form()

