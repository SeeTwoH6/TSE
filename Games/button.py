import tkinter as tk

class Button:
    def __init__(self, parent, text, x, y):
        #creates button
        self.button = tk.Button(parent, text=text, command=None, borderwidth=0)
        #places button in a place stated
        self.button.place(x=x, y=y)
    
    #changes the buttons colour
    def button_colour(self, button_colour):
        self.button.config(bg=button_colour)

    #changes the buttons text colour
    def text_colour(self, text_colour):
        self.button.config(fg=text_colour)
    
    #sets the action for the button 
    def action(self, action):
        self.button.config(command=action)

    #changes the font of the button
    def font(self, font):
        self.button.config(font=font)

    #changes size of the button
    def size(self, height, width):
        self.button.config(height=height, width=width)

    def delete(self):
        self.button.destroy()