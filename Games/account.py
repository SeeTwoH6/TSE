import tkinter as tk
from tkinter import messagebox
import mysql.connector
import GUI
import button as bt

class Account:
    def __init__(self, root):
        self.root = root
        self.GUI = GUI.GUI(self.root)

    def register_GUI(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        title = tk.Label(self.root, text = "Register", font=("arial", 15, "bold"), fg="dark blue")
        #places title at the top
        title.place(x= 12, y=0)
        #outputs the title
        title.pack()
        labels = ["First Name", "Last Name", "Password", "Email", "DateOfBirth", "Age", "Gender", "Height", "Weight"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(self.root, text=label + ":", anchor="w").pack()
            entry = tk.Entry(self.root)
            entry.pack()
            entries.append(entry)

        def submit():
            values = [e.get() for e in entries]
            self.addUserToDatabase(*values)
            self.GUI.mainMenu()

        login_link = tk.Label(self.root, text="go to login", fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
        login_link.pack(pady=30)
        login_link.bind("<Button-1>", lambda e: self.login_GUI())
        submit_button = bt.Button(self.root, "Submit", 13, 500)
        submit_button.size(2, 47)
        submit_button.button_colour("dark blue")
        submit_button.text_colour("white")
        submit_button.action(submit)

    def login(self, email, password):
        result = ""
        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host="192.168.152.160",  
                user="27738139",       
                password="27738139EL",  
                database="healthapp"    
            )
            cursor = conn.cursor()
            # Insert statement

            if not email or not password:
                messagebox.showerror("Error", "please enter a valid email and/or password")
            query = "SELECT UserID from healthapp.users WHERE email = %s AND password =%s"
            cursor.execute(query, (email, password))

            print("Data inserted successfully.")

            result = cursor.fetchone()[0]
            if result:
                messagebox.showinfo("Login Successful")
            else:
                messagebox.showerror("Invalid email and/or password")


        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Database Connection Error: {error}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        return result

    
    def login_GUI(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        
        title = tk.Label(self.root, text = "Login", font=("arial", 15, "bold"), fg="dark blue")
        #places title at the top
        title.grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="Email:", font=("Arial", 12)).grid(row=1, column=0, pady=20, sticky="e")
        email_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        email_entry.grid(row=1, column=1, pady=20)
        
        tk.Label(self.root, text="Password:", font=("Arial", 12)).grid(row=2, column=0, pady=10, sticky="e")
        password_entry = tk.Entry(self.root, width=30, show="*", font=("Arial", 12))
        password_entry.grid(row=2, column=1, pady=20)

        def attempt_login():
            email = email_entry.get()
            password = password_entry.get()
            self.login(email, password)
            self.GUI.mainMenu()

        register_link = tk.Label(self.root, text="Don't have an account? Register here", fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
        register_link.grid(row=3, column=0, columnspan=2, pady=10)
        register_link.bind("<Button-1>", lambda e: self.register_GUI())
        submit_button = bt.Button(self.root, "Submit", 13, 500)
        submit_button = bt.Button(self.root, "Submit", 13, 500)
        submit_button.size(2, 47)
        submit_button.button_colour("dark blue")
        submit_button.text_colour("white")
        submit_button.action(attempt_login)

    def addUserToDatabase(self, firstName, lastName, password, email, DOB, age, gender, height, weight):
            try:
                # Connect to the MySQL database
                conn = mysql.connector.connect(
                    host="192.168.152.160",  
                    user="27738139",       
                    password="27738139EL",  
                    database="healthapp"    
                )
                print(f"Conn: {conn}")
                cursor = conn.cursor()

                # Insert statement
                query = "SELECT IFNULL((SELECT (MAX(UserID) +1) FROM healthapp.users), '1')"
                cursor.execute(query)
                userID = cursor.fetchone()[0]
                query = "INSERT INTO healthapp.users (UserID, FirstName, LastName, Password, Email, DateOfBirth, Age, Gender, Height, Weight) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (userID, firstName, lastName, password, email, DOB, age, gender, height, weight))
                conn.commit()

                print("Data inserted successfully.")

            except mysql.connector.Error as error:
                messagebox.showerror("Error", f"Database Connection Error: {error}")
            except mysql.connector.IntegrityError as error:
                messagebox.showerror("Error", "Email has already been used")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()


def main():
    root = tk.Tk()
    root.geometry("400x600")
    app = Account(root)
    app.register_GUI()
    root.mainloop()

if __name__ == "__main__":
    main()