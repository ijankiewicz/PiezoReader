import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import re

import numpy as np

f = open("tag6.txt", "r")
title = f.readline(0)
contents = f.readlines()[1:]

line2 = []
step2 = []
val21 = []
val22 = []

# COUNT SAMPLES
sample_count = 0
for line in contents:
    line2.append("0")
    step2.append("0")
    val21.append("0")
    val22.append("0")
    line2[sample_count] = re.split('\t|,', contents[sample_count].strip("\n").strip(')').replace('(', ''))
    step2[sample_count] = float(line2[sample_count][0])
    val21[sample_count] = line2[sample_count][1]
    val22[sample_count] = line2[sample_count][2]
    
    if 'dB' in val21[sample_count]:
        val21_unit = 'dB'
        val21[sample_count] = val21[sample_count].strip('dB')
        val21[sample_count] = float(val21[sample_count])

    val22[sample_count] = line2[sample_count][2]
    if '°' in val22[sample_count]:
        val22[sample_count] = float(val22[sample_count].strip('°'))

    # print(val21[sample_count])

    sample_count += 1

step2 = np.asarray(step2, dtype=np.float)
val21 = np.asarray(val21, dtype=np.float)
val22 = np.asarray(val22, dtype=np.float)
    
f.close()

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
fig.add_subplot(111).plot(step2, val21)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.