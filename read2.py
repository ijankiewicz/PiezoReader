import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
import re
import numpy as np
import os
import pathlib

from collections import namedtuple

class Application:
    def __init__(self):

        # Set fixed geometry and the title of the main window
        self.window = tk.Tk()
        self.window.geometry("400x30")
        self.window.resizable(0, 0)
        self.window.title("LTspice text data to .csv converter v1.0")

        # Create button
        openButton = tk.Button(self.window,text='Open', command = self.open_file)
        openButton.grid(column=0,row=0)
        openButton.pack()
 
        self.window.mainloop()

    def open_file(self):
        # invoke "Open File" dialog window
        filename = fd.askopenfilename(filetypes=[("Text file","*.txt")])

        if filename:

            f = open(filename, 'r')
            contents = f.readlines()[1:]

            rawLine = []
            
            # COUNT SAMPLES
            sampleCount = 0
            for line in contents:
                rawLine.append("0")
                rawLine[sampleCount] = re.split('\t|,', contents[sampleCount].strip("\n").strip(')').replace('(', ''))
                columnCount = len(rawLine[0])
                rawData = []
                rawData.append("0")
            
                # remove unwanted characters
                for column in range(columnCount):

                    if 'dB' in rawLine[sampleCount][column]:
                        rawLine[sampleCount][column] = rawLine[sampleCount][column].strip('dB')

                    if '°' in rawLine[sampleCount][column]:
                        rawLine[sampleCount][column] = rawLine[sampleCount][column].strip('°')
                
                sampleCount += 1

            rawLine = np.array(rawLine, dtype=float)

            np.savetxt("temp.csv", rawLine, delimiter=',')
            os.system("attrib +h temp.csv")

            f.close()
            self.saveFile()
            self.openButtonClicked()

    def openButtonClicked(self):
        messagebox.showinfo('Info', 'Data has been converted')

    def saveFile(self):
            filename = fd.asksaveasfilename(filetypes=[("Comma-separated values file","*.csv")], defaultextension = "*.csv") # wywołanie okna dialogowego save file
            f = open("temp.csv", "r")
            data = f.read()
            if filename:
                with open(filename, "w") as file:
                    file.write(data)
            f.close()
            os.remove("temp.csv")



apl = Application()