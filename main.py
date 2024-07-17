import database
import empform


database.connect_db()
database.initialize_constants()

empform.show_employee_form()

