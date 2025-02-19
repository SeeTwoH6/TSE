import tkinter as tk
import button as bt

class GUI:
    def __init__(self):
        #creates tkinter window
        self.root = tk.Tk()
        #signals the screen size
        self.root.geometry("360x640")
        #makes it so that the window size cannot be altered
        self.root.resizable(False, False)

    def mainMenu(self):
        #creates title
        title = tk.Label(self.root, text = "Home", font=("arial", 15, "bold"), fg="dark blue")
        #places title at the top
        title.place(x= 12, y=0)
        #outputs title
        title.pack()

        #creates menu button
        menu_btn = bt.Button(self.root, "≡", 12, 0)
        menu_btn.button_colour("white")
        menu_btn.text_colour("dark blue")
        menu_btn.font(("arial, 13"))
        menu_btn.action(self.Navigation_btn())


        #health stats block summary
        stats_block = tk.Frame(self.root, bg="light grey", width=500, height=200)
        stats_block.place(x=0, y=40)

        #creates excercise button
        excecise_btn = bt.Button(self.root, "Cognative Excercises", 12, 270)
        excecise_btn.button_colour("Dark Blue")
        excecise_btn.text_colour("white")
        excecise_btn.size(2, 47)

        #creates calorie button
        calorie_btn = bt.Button(self.root, "Calorie intake", 12, 310)
        calorie_btn.button_colour("Dark Blue")
        calorie_btn.text_colour("white")
        calorie_btn.size(2, 47)

        #creates water intake button
        water_btn = bt.Button(self.root, "Water Intake", 12, 350)
        water_btn.button_colour("Dark Blue")
        water_btn.text_colour("white")
        water_btn.size(2, 47)

        #creates excercise activity button
        exercise_btn = bt.Button(self.root, "Exercise Activity", 12, 390)
        exercise_btn.button_colour("Dark Blue")
        exercise_btn.text_colour("white")
        exercise_btn.size(2, 47)

        #creates heart rate monitor button
        heart_btn = bt.Button(self.root, "Heart Rate Monitor", 12, 430)
        heart_btn.button_colour("Dark Blue")
        heart_btn.text_colour("white")
        heart_btn.size(2, 47)

        #creates sleep analysis button
        sleep_btn = bt.Button(self.root, "Sleep Analysis", 12, 470)
        sleep_btn.button_colour("Dark Blue")
        sleep_btn.text_colour("white")
        sleep_btn.size(2, 47)

        #creates the chatbox input (TBA) 
        chat_box = tk.Entry(self.root, bg="light grey", fg="grey", borderwidth=0, width=58)
        chat_box.place(x=5, y=575)
        
    #gives functionality to the navigation button
    def Navigation_btn(self):
        stats_block = tk.Frame(self.root, bg="white", width=600, height=360)
        stats_block.place(x=0, y=20)
