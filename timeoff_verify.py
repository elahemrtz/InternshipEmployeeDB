import tkinter as tk
from tkinter import messagebox



TIMEOFF_REQUESTS = 
    {"emp_id": "123", "name": "John Doe", "type": "Daily", "date": "2024-07-28", "start_date": "2024-07-28", "end_date": "2024-07-29", "start_time": "", "end_time": ""},
    {"emp_id": "456", "name": "Jane Smith", "type": "Hourly", "date": "2024-07-09", "start_date": "2024-07-26", "end_date": "2024-07-26", "start_time": "09:00", "end_time": "13:00"},
    {"emp_id": "789", "name": "Alice Johnson", "type": "Daily", "date": "2024-07-29", "start_date": "2024-07-28", "end_date": "2024-07-29", "start_time": "", "end_time": ""}
]

class TimeoffVerification(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timeoff Verification")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Timeoff Requests", font=('Arial', 16)).pack(pady=10)

        self.requests_frame = tk.Frame(self)
        self.requests_frame.pack(fill=tk.BOTH, expand=True)

        for req in TIMEOFF_REQUESTS:
            frame = tk.Frame(self.requests_frame)
            frame.pack(fill=tk.X, padx=10, pady=5)

            tk.Label(frame, text=f"Employee ID: {req['emp_id']}, Name: {req['name']}").pack(side=tk.LEFT, padx=10)

            view_button = tk.Button(frame, text="View Details", command=lambda r=req: self.view_details(r))
            view_button.pack(side=tk.RIGHT, padx=10)
            

    def view_details(self, request):
        details_window = tk.Toplevel(self)
        details_window.title("Timeoff Details")
        details_window.geometry("300x300")

        tk.Label(details_window, text=f"Employee ID: {request['emp_id']}").pack(pady=10)
        tk.Label(details_window, text=f"Name: {request['name']}").pack(pady=10)
        tk.Label(details_window, text=f"Leave Type: {request['type']}").pack(pady=10)

        if request['type'] == "Daily":
            tk.Label(details_window, text=f"Date: {request['date']}").pack(pady=10)
            tk.Label(details_window, text=f"Start Date: {request['start_date']}").pack(pady=10)
            tk.Label(details_window, text=f"End Date: {request['end_date']}").pack(pady=10)
        else:
            tk.Label(details_window, text=f"Date: {request['date']}").pack(pady=10)
    
            tk.Label(details_window, text=f"Start Time: {request['start_time']}").pack(pady=10)
            tk.Label(details_window, text=f"End Time: {request['end_time']}").pack(pady=10)

        approve_button = tk.Button(details_window, text="Approve", command=lambda: self.process_request(request, "approved"))
        approve_button.pack(side=tk.LEFT, padx=20, pady=20)

        reject_button = tk.Button(details_window, text="Reject", command=lambda: self.process_request(request, "rejected"))
        reject_button.pack(side=tk.RIGHT, padx=20, pady=20)

    def process_request(self, request, action):
        if action == "approved":
            messagebox.showinfo("Request Approved", f"Request for {request['name']} has been approved.")
        else:
            messagebox.showinfo("Request Rejected", f"Request for {request['name']} has been rejected.")
        self.refresh_requests()

    def refresh_requests(self):
        self.destroy()
        self.__init__()
        self.mainloop()

if __name__ == "__main__":
    app = TimeoffVerification()
    app.mainloop()