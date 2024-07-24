import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class VerifyLeave :
    def __init__(self,root):
        self.root=root        
        self.root.title("Leave Request Verify")
        

        self.create_widgets()

    def create_widgets(self):
        