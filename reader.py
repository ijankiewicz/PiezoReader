from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import re
import numpy as np

f = open("data1.txt", "r")
title = f.readline(0)
contents = f.readlines()[1:]

line2 = {}
step2 = {}
val21 = {}
val22 = {}
# COUNT SAMPLES
sample_count = 0
for line in contents:
    line2[sample_count] = re.split('\t|,', contents[sample_count].strip("\n").strip(')').replace('(', ''))
    step2[sample_count] = float(line2[sample_count][0])
    val21[sample_count] = line2[sample_count][1]
    val22[sample_count] = line2[sample_count][2]
    
    if 'dB' in val21[sample_count]:
        val21_unit = 'dB'
        val21[sample_count] = val21[sample_count].strip('dB')
        val21[sample_count] = float(val21[sample_count])

    val22[sample_count] = line2[sample_count][2]
    if 'ďż˝' in val22[sample_count]:
        val22[sample_count] = float(val22[sample_count].strip('ďż˝'))

    # print(val21[sample_count])

    sample_count += 1

step2 = np.asarray(step2)
val21 = np.asarray(val21)
val22 = np.asarray(val22)
print(val21)
print(val22)

print(line2)
# REMOVE RUBBISH FROM DATA
line = re.split('\t|,', contents[1].strip("\n").strip(')').replace('(', ''))
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
