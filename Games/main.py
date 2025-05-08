import tkinter
import GUI
import account

def main():
    #creates a window
    root = tkinter.Tk()
    #debug()
    #emulates a phone screen menu size
    root.geometry("360x640")
    root.resizable(False, False)
    gui = GUI.GUI(root)
    gui.mainMenu()
    #GUI loop
    root.mainloop()

def debug():
    #... signifies to be added/ TBC
    print(f" 1. game \n 2. AI testing \n 3. calorie tracker \n 4. GUI \n")
    debug_input = input(" ")

    #add it on when finished
    #if debug_input == 1:
    #    ...
    #if debug_input == 2:
    #    ...
    #if debug_input == 3:
    #    ...
    if debug_input == 4:
        ...
        


if __name__ == "__main__":
    main()

