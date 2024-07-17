import tkinter as tk
from tkinter import *

class UserProfileApp:
    def _init_(self , root):
        self.root = root
        self.root.title("Employee List")

        self.users = ["A" , "B" , "C"]

        self.create_widget()

    def create_widget(self):
        for idx , user in enumerate(self.users):
            lbl_user = tk.Label(self.root)
            lbl_user.grid(row=idx, column=0, padx=10, pady=5)
            
            btn_view_profile = tk.Button(self.root, text="View Salary", command=lambda u=user: self.open_profile(u))
            
            btn_view_profile.grid(row=idx, column=2, padx=10, pady=5)

    
    def open_profile(self, user):
        profile_window = tk.Toplevel(self.root)
        profile_window.title(f"{user}'s Salary")
        
        lbl_user_name = tk.Label(profile_window, text=f"Name: {user}")
        lbl_user_name.pack(padx=10, pady=10)

        # Additional profile information can be added here
        lbl_profile_info = tk.Label(profile_window, text=f"Salary info for {user} goes here.")
        lbl_profile_info.pack(padx=10, pady=10)   


if __name__ == "__main__":

#connect to database 

#get list of employees 

#call function to compute total
    


    root = tk.Tk()
    app = UserProfileApp()
    app._init_(root=root)
    root.mainloop()    

