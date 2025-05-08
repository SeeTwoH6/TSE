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

    def addUserToDatabase(firstName, lastName, password, email, DOB, age, gender, height, weight):
            try:
                # Connect to the MySQL database
                conn = mysql.connector.connect(
                    host="192.168.149.185",  
                    user="27738139",       
                    password="27738139EL",  
                    database="healthapp"    
                )
                cursor = conn.cursor()

                # Insert statement
                query = "SELECT IFNULL((SELECT (MAX(UserID) +1) FROM healthapp.user), '1')"
                cursor.execute(query)
                userID = cursor.fetchone()[0]
                query = "INSERT INTO healthapp.user (UserID, FirstName, LastName, Password, Email, DateOfBirth, Age, Gender, Height, Weight) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (userID, firstName, lastName, password, email, DOB, age, gender, height, weight))
                conn.commit()

                print("Data inserted successfully.")

            except mysql.connector.Error as error:
                print(f"Database Connection Error: {error}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()


