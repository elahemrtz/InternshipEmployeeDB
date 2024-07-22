import database
import empform
import timesheet
import salary


database.connect_db()
database.initialize_constants()

#timesheet.TimesheetApp()
#empform.EmployeeForm()
salary.UserProfileApp()
