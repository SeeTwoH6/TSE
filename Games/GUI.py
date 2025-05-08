import tkinter as tk
import Counting.Counting
import button as bt
from water import waterIntake
import calorie as cl
import Counting
import Memory
import Reaction
import account
import AIBodyTracker

class GUI:
    def __init__(self, root):
        #creates tkinter window
        self.root = root
    
    #function destroys all widgets in the window
    def destroy_widgets(self):
        #gets the all widget in the window
        for widget in self.root.winfo_children():
            #destroys all widgets in the window 
            widget.destroy()

    def mainMenu(self):

        self.destroy_widgets()
        #creates title
        title = tk.Label(self.root, text = "Home", font=("arial", 15, "bold"), fg="dark blue")
        #places title at the top
        title.place(x= 12, y=0)
        #outputs title
        title.pack()

        self.navigation_btn()

        #health stats block summary
        stats_block = tk.Frame(self.root, bg="light grey", width=500, height=200)
        stats_block.place(x=0, y=40)

        #creates excercise button
        excecise_btn = bt.Button(self.root, "Cognative Excercises", 12, 270)
        excecise_btn.button_colour("Dark Blue")
        excecise_btn.text_colour("white")
        excecise_btn.size(2, 47)
        excecise_btn.action(self.cognative_excercises)

        #creates calorie button
        calorie_btn = bt.Button(self.root, "Calorie intake", 12, 310)
        calorie_btn.button_colour("Dark Blue")
        calorie_btn.text_colour("white")
        calorie_btn.size(2, 47)
        calorie_btn.action(self.foodIntake)

        #creates water intake button
        water_btn = bt.Button(self.root, "Water Intake", 12, 350)
        water_btn.button_colour("Dark Blue")
        water_btn.text_colour("white")
        water_btn.size(2, 47)
        water_btn.action(self.waterIntake)

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

    def navigation_btn(self):
        #creates a menu button
        menubar = tk.Menu(self.root)

        menu = tk.Menu(menubar, tearoff=0)
        menu.add_command(label="Home", command=self.mainMenu)
        menu.add_command(label = "Cognative Excercises", command=self.cognative_excercises)
        menu.add_command(label="Water Intake", command = self.waterIntake)
        menu.add_command(label="Calorie Intake", command = self.foodIntake)
        menu.add_command(label="Exercise Activity")
        menu.add_command(label="Heart Rate Monitor")
        menu.add_command(label="sleep analysis")
        menubar.add_cascade(label="menu", menu=menu)

        menubar.config(font=("Arial", 30))
        self.root.config(menu=menubar)

    def exercise_activity(self):
        self.destroy_widgets()
        #creates title
        title = tk.Label(self.root, text = "Exercise Tracker", font=("arial", 15, "bold"), fg="dark blue")
        #places title at the top
        title.place(x= 12, y=0)
        #outputs the title
        title.pack()
        self.navigation_btn()

        exercise_btn = bt.Button(self.root, "Exercise Activity", 12, 270)
        exercise_btn.button_colour("Dark Blue")
        exercise_btn.text_colour("white")
        exercise_btn.size(2, 47)
        exercise_btn.action(AIBodyTracker.exercise())

    def cognative_excercises(self):
        self.destroy_widgets()
        #creates title
        title = tk.Label(self.root, text = "cognative excercise", font=("arial", 15, "bold"), fg="dark blue")
        #places title at the top
        title.place(x= 12, y=0)
        #outputs title
        title.pack()

        self.navigation_btn()

        """
        more functionality for these buttons will be added later
        """
        #health stats block summary
        stats_block = tk.Frame(self.root, bg="light grey", width=500, height=200)
        stats_block.place(x=0, y=40)

        #creates a counting game button
        counting_btn = bt.Button(self.root, " Counting Excercises", 12, 270)
        counting_btn.button_colour("Dark Blue")
        counting_btn.text_colour("white")
        counting_btn.size(2, 47)
        counting_btn.action(Counting.Counting.counting_game)

        #creates balencing game button
        balencing_btn = bt.Button(self.root, "Balencing Excercise", 12, 310)
        balencing_btn.button_colour("Dark Blue")
        balencing_btn.text_colour("white")
        balencing_btn.size(2, 47)

        #creates memory game button
        memory_btn = bt.Button(self.root, "Memory Excerise", 12, 350)
        memory_btn.button_colour("Dark Blue")
        memory_btn.text_colour("white")
        memory_btn.size(2, 47)
        memory_btn.action(Memory.launch_game)

        #creates reaction game button
        reaction_btn = bt.Button(self.root, "Reaction Excerise", 12, 390)
        reaction_btn.button_colour("Dark Blue")
        reaction_btn.text_colour("white")
        reaction_btn.size(2, 47)
        reaction_btn.action(Reaction.reaction_game)


    def waterIntake(self):
        self.destroy_widgets()
        #creates title
        title = tk.Label(self.root, text = "Water Intake", font=("arial", 15, "bold"), fg="dark blue")
        #places title at the top
        title.place(x= 12, y=0)
        #outputs the title
        title.pack()
        self.navigation_btn()
        self.water_intake = waterIntake(self.root)
        self.water_intake.create_GUI()

    def foodIntake(self):
        self.destroy_widgets()
        #creates the calories intake GUI
        self.calorie_intake = cl.CalorieIntake(self.root)
        self.calorie_intake.create_GUI()

    def register(self):
        self.destroy_widgets()
        self.account = account.Account(self.root)
        self.account.register_GUI()
        
    def login(self):
        if not hasattr(self, 'account'):
            self.account = account.Account(self.root)
        self.account.login_GUI()

    

    











