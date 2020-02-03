from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class GUI:
    def __init__(self,master):
        self.master = master
        master.title("Piezo Reader GUI")

        # BUTTONS
        self.start_button = Button(master, text = "Start", fg = "Blue")
        self.stop_button = Button(master, text = "Stop", fg = "Black")
        self.options_button = Button(master, text = "Options", fg = "Black")

        # LAYOUT
        self.start_button.grid(row=2, column=0)
        self.stop_button.grid(row=2, column=1)
        self.options_button.grid(row=2, column=2, sticky=W+E)


root = Tk()
piezo_gui = GUI(root)
root.mainloop()
