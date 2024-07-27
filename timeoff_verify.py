import tkinter as tk
from tkinter import messagebox
from database import *

class TimeoffVerification:
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title("Timeoff Verification")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Timeoff Requests", font=('Arial', 16)).pack(pady=10)

        self.requests_frame = tk.Frame(self.root)
        self.requests_frame.pack(fill=tk.BOTH, expand=True)

        for id, emp_id, type, start_time, end_time, _, accepted, declined, name in self.fetch_timeoffs():
            req = {'id': id, 'emp_id': emp_id, 'name': name, 'type': type}
            if type == 'Daily':
                req['start_date'] = start_time.date()
                req['end_date'] = end_time.date()
            else:
                req['date'] = start_time.date()
                req['start_time'] = start_time.time()
                req['end_time'] = end_time.time()
            frame = tk.Frame(self.requests_frame)
            frame.pack(fill=tk.X, padx=10, pady=5)

            tk.Label(frame, text=f"ID: {req['id']}, Name: {req['name']}").pack(side=tk.LEFT, padx=10)

            view_button = tk.Button(frame, text="View Details", command=lambda r=req: self.view_details(r))
            view_button.pack(side=tk.RIGHT, padx=10)
            
    def fetch_timeoffs(self):
        return select_query('select t.*, e.first_name || \' \' || e.last_name as name from timeoff t left join employee e on t.employee=e.id')

    def view_details(self, request):
        details_window = tk.Toplevel(self.root)
        details_window.title("Timeoff Details")
        details_window.geometry("300x300")

        tk.Label(details_window, text=f"Employee ID: {request['emp_id']}").pack(pady=10)
        tk.Label(details_window, text=f"Name: {request['name']}").pack(pady=10)
        tk.Label(details_window, text=f"Leave Type: {request['type']}").pack(pady=10)

        if request['type'] == "Daily":
            tk.Label(details_window, text=f"Start Date: {request['start_date']}").pack(pady=10)
            tk.Label(details_window, text=f"End Date: {request['end_date']}").pack(pady=10)
        else:
            tk.Label(details_window, text=f"Date: {request['date']}").pack(pady=10)
            tk.Label(details_window, text=f"Start Time: {request['start_time']}").pack(pady=10)
            tk.Label(details_window, text=f"End Time: {request['end_time']}").pack(pady=10)

        approve_button = tk.Button(details_window, text="Accept", command=lambda: self.process_request(request, "accepted"))
        approve_button.pack(side=tk.LEFT, padx=20, pady=20)

        reject_button = tk.Button(details_window, text="Decline", command=lambda: self.process_request(request, "declined"))
        reject_button.pack(side=tk.RIGHT, padx=20, pady=20)

    def process_request(self, request, action):
        other = 'declined' if action == 'accepted' else 'accepted'
        query(f'update timeoff set {action}=1, {other}=0 where id={request['id']}')
        messagebox.showinfo(f"Request {action}", f"Request for {request['name']} has been {action}.")
        
if __name__ == "__main__":
    app = TimeoffVerification(tk.Tk())
    app.mainloop()