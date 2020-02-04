from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import re

f = open("data2.txt", "r")
title = f.readline()
contents = f.readlines()[1:]

# COUNT SAMPLES
sample_count = 0
for line in contents:
    sample_count += 1

# REMOVE RUBBISH FROM DATA
line = re.split('\t|,', contents[0].strip("\n").strip(')').replace('(', ''))
step = float(line[0])

# LOOK FOR SPECIAL CHARRACTERS AND UNITS
val1 = line[1]
if 'dB' in val1:
    val1_unit = 'dB'
    val1 = val1.strip('dB')
    val1 = float(val1)

val2 = line[2]
if 'ďż˝' in val2:
    val2 = float(val2.strip('ďż˝'))



print(title)
print(step)
print(val1)
print(val2)

f.close()

fig = Figure(figsize=(5, 4), dpi=100)
t = data
fig.add_subplot(111).plot(sample_count, data)

class GUI:
    def __init__(self,master):
        self.master = master
        master.title("Piezo Reader GUI")

        self.canvas = FigureCanvasTkAgg(fig)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.toolbar = NavigationToolbar2Tk(canvas, root)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)


        self.canvas.mpl_connect("key_press_event", on_key_press)

        # BUTTONS
        self.start_button = Button(master, text = "Start", fg = "Blue")
        self.stop_button = Button(master, text = "Stop", fg = "Black")
        self.options_button = Button(master, text = "Options", fg = "Black")
        self.quit_button = Button(master, text = "Quit", fg = "Black", command = _quit)

        # LAYOUT
        self.start_button.grid(row=2, column=0)
        self.stop_button.grid(row=2, column=1)
        self.options_button.grid(row=2, column=2, sticky=W+E)
        self.quit_button.grid(row=3, column=2, sticky=W+E)

    def _quit():
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate


root = Tk()
piezo_gui = GUI(root)
root.mainloop()
