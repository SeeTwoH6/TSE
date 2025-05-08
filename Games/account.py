import tkinter as tk
from tkinter import messagebox
import mysql.connector
import GUI
import button as bt

class Account:
    def __init__(self, root):
        self.root = root

    def register_user(self, first_name, last_name, email, password, dateOfBirth, age, gender, height, weight):
        self.GUI = GUI.GUI(self.root)
        ...
        #call main using self.GUI.mainMenu() when registering is successful

    def register_GUI(self):

        labels = ["First Name", "Last Name", "Email", "Password","Date Of Birth", "Age", "Gender", "Height", "Weight"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(self.root, text=label + ":", anchor="w").pack()
            entry = tk.Entry(self.root)
            entry.pack()
            entries.append(entry)

            def submit():
                values = [e.get() for e in entries]
                self.register_user(*values)

            submit_button = bt.Button(self.root, "Submit", 13, 500)
            submit_button.size(2, 47)
            submit_button.button_colour("dark blue")
            submit_button.text_colour("white")
            submit_button.action(submit)

    def login (self, username, password):
        ...
        #call main using self.GUI.mainMenu() when login is successful

    
    def login_GUI(self):

        tk.Label(self.root, text="Email:").grid(row=0, column=0, sticky="w")
        email_entry = tk.Entry(self.root, width=30)
        email_entry.grid(row=0, column=1)
        
        tk.Label(self.root, text="Password:").grid(row=1, column=0, sticky="w")
        password_entry = tk.Entry(self.root, width=30)
        password_entry.grid(row=1, column=1)

        def attempt_login():
            email = email_entry.get()
            password = password_entry.get()
            self.login_user(email, password)

        submit_button = bt.Button(self.root, "Submit", 13, 500)
        submit_button.size(2, 47)
        submit_button.button_colour("dark blue")
        submit_button.text_colour("white")
        submit_button.action(attempt_login)




