import tkinter as tk
import GUI
import button as bt

class waterIntake:

    def __init__(self, root):
        self.total_intake = 0
        self.root = root
        self.Capacity = 2000
        self.canvas = tk.Canvas(self.root, width=360, height=400, bg="white")
    def create_GUI(self):
        self.canvas.pack()
        #draws glass in canvas
        self.left_x = 130
        self.right_x = 230
        self.top_y = 150
        self.bottom_y = 350
        self.canvas.create_line(self.left_x, self.top_y, self.left_x, self.bottom_y, fill="black", width=2)
        self.canvas.create_line(self.right_x, self.top_y, self.right_x, self.bottom_y, fill="black", width=2)
        self.canvas.create_line(self.left_x, self.bottom_y, self.right_x, self.bottom_y, fill="black", width=2)

        self.water_rect = self.canvas.create_rectangle(self.left_x +2, self.bottom_y, self.right_x - 2, self.bottom_y, fill="blue", width=0)
        
        self.intake_label = tk.Label(self.root, text=f"Total intake: {self.total_intake} ml")
        self.intake_label.pack()
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=10)

        submit_btn = bt.Button(self.root, "Submit", 12, 500)
        submit_btn.button_colour("Dark Blue")
        submit_btn.text_colour("white")
        submit_btn.size(2, 47)
        submit_btn.action(self.add_intake)

    def add_intake(self):
        try:
            #gets input from user
            val = int(self.entry.get())
            #if value isnt above 0 it will return an error
            if val < 0:
                self.intake_label.config(text="enter a number above 0")
                return       
            #adds to total intake
            self.total_intake += val

            if self.total_intake >= self.Capacity:
                self.total_intake = self.Capacity
                self.intake_label.config(text=f"you have drank the max amount of water today")
                return

            water_height = (self.total_intake/self.Capacity) *200
            new_top_y = self.bottom_y - water_height

            self.canvas.coords(self.water_rect, self.left_x+2, new_top_y, self.right_x - 2, self.bottom_y)
            self.intake_label.config(text=f"Total water intake: {self.total_intake} ml")
            self.entry.delete(0, tk.END)
        #prevents any invalid errors
        except ValueError:
            self.intake_label.config(text="Enter a valid number")
        
