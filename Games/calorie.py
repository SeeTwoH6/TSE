import tkinter as tk
import math
import button as bt
import GUI
import threading
import test as t
class CalorieIntake():
    def __init__(self, root):
        self.root = root
        self.colors = ["red", "green", "blue"]
        self.intake = {
            "Fat (g)": 1,
            "Carbohydrates (g)": 1,
            "Protein (g)": 1
        }
        self.food_dict = []
        self.tempGUI = GUI.GUI(self.root)


    #temp food list
    def get_food_text_file(self):
        file_path = "food_nutrition_list.txt"
        
        with open(file_path, "r") as f:
            lines = f.readlines()

        header = lines[0].strip().split("\t")[1:]

        self.food_dict = {}
        for line in lines[1:]:
            parts = line.strip().split("\t")
            foodname = parts[0]
            nutrients = {header[i]: float(parts[i+1]) for i in range (len(header))}
            self.food_dict[foodname] = nutrients
        
    
    #creates a new GUI
    def create_GUI(self):
        title = tk.Label(self.root, text = "Calorie Intake", font=("arial", 15, "bold"), fg="dark blue")
        #places title at the top
        title.place(x= 12, y=0)
        #outputs the title
        title.pack()
        self.tempGUI.navigation_btn()
        self.canvas = tk.Canvas(self.root, width=360, height=400, bg="white")
        self.canvas.delete("all")
        self.canvas.pack()
        total = sum(self.intake.values())
        self.radius = 100
        x_centre = 360 / 2
        y_centre = 400 / 2
        x0 = x_centre - self.radius
        y0 = y_centre - self.radius - 50
        x1 = x_centre + self.radius
        y1 = y_centre + self.radius - 50
        
        start_angle = 0
        for i, (label, value) in enumerate(self.intake.items()):
            extent = (value / total) * 360
            self.canvas.create_arc(x0, y0, x1, y1, start = start_angle, extent=extent, fill=self.colors[i])

            mid_angle = math.radians(start_angle + extent / 2)
            
            label_text = f"{label} {value}"
            text_offset = 0

            if 225 < mid_angle >= 315:
                text_offset = 25
            else:
                text_offset = 0

            label_x = x_centre + (self.radius + text_offset) * math.cos(mid_angle)
            label_y = y_centre - (self.radius + text_offset) * math.sin(mid_angle)
            anchor = "w" if math.cos(mid_angle) >= 0 else "e"
            self.canvas.create_text(label_x, label_y, text=label_text, font=("Arial", 10), fill=self.colors[i], anchor=anchor)
            start_angle += extent

        #creates a breakfast button
        breakfast_button = bt.Button(self.root, "breakfast", 13, 350)
        breakfast_button.button_colour("dark blue")
        breakfast_button.text_colour("white")
        breakfast_button.size(2, 47)

        #creates a lunch button
        lunch_button = bt.Button(self.root, "Lunch", 13, 400)
        lunch_button.button_colour("dark blue")
        lunch_button.text_colour("white")
        lunch_button.size(2, 47)

        #creates dinner button
        dinner_button = bt.Button(self.root, "Dinner", 13, 450)
        dinner_button.button_colour("dark blue")
        dinner_button.text_colour("white")
        dinner_button.size(2, 47)

        #creates a snack button
        snack_button = bt.Button(self.root, "snack", 13, 500)
        snack_button.button_colour("dark blue")
        snack_button.text_colour("white")
        snack_button.size(2, 47)
        #opens the foodlist GUI 
        breakfast_button.action(self.food_list_GUI)
        lunch_button.action(self.food_list_GUI)
        dinner_button.action(self.food_list_GUI)
        snack_button.action(self.food_list_GUI)

    #creates food list GUI
    def food_list_GUI(self):
        self.tempGUI.destroy_widgets()
        self.get_food_text_file()
        #creates a list
        food_listbox = tk.Listbox(self.root, font=("Arial, 12"), height=50, width=360, selectmode="single")
        food_listbox.pack(pady=10)
        for food in self.food_dict:
            food_listbox.insert(tk.END, food)
        
        def confirm_selection():
            selection = food_listbox.curselection()

            for i in selection:
                food_name = food_listbox.get(i)
                for key in self.intake:
                    value = self.food_dict[food_name][key]
                    self.intake[key] += value
            
            food_listbox.destroy()
            confirm_button.delete()
            self.create_GUI()
        
        #creates a confirm button
        confirm_button = bt.Button(self.root, "confirm", 13, 500)
        confirm_button.button_colour("dark blue")
        confirm_button.text_colour("white")
        confirm_button.size(2, 47)
        confirm_button.action(confirm_selection)

        


