import tkinter as tk
from tkinter import filedialog as fd
import re
import numpy as np
import os
import pathlib

from collections import namedtuple

class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("100x100")
        self.window.title("LTspice text data to .csv")

        # Create buttons

        openButton = tk.Button()

        # tworzenie menu

        self.menu = tk.Menu(self.window)
        
        submenu = tk.Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = "Plik", menu = submenu)
        
        submenu.add_command(label = "Otwórz", command = self.open_file)
        submenu.add_command(label = "Zapisz", command = self.save_file)
        
        self.window.config(menu = self.menu, width = 50, height = 30)

        # dodawanie kontrolki typu Text i paska przewijania
        
        self.text = tk.Text(self.window)
        
        self.sb_text = tk.Scrollbar(self.window)
        self.sb_text.place(in_ = self.text, relx = 1., rely = 0, relheight = 1.)
        self.sb_text.config(command = self.text.yview)
        self.text.config(yscrollcommand = self.sb_text.set)
        
        self.text.place(x = 0, y = 0, relwidth = 1, relheight = 1, width = - 18)
        
        self.window.mainloop()

    def open_file(self):
        # invoke "Oppen FIle" dialog window
        filename = fd.askopenfilename(filetypes=[("Plik tekstowy","*.txt")])
        # determine the output file
        outputFile = pathlib.Path("output.csv")
        # check if the output file already exists. If not, create it first
        if outputFile.exists():
            pass
        else:
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            os.path.join(THIS_FOLDER, 'output.csv')
            print("Output file has been created")
        # clear output file contents before next write sequence
        open('output.csv', 'w').close()

        if filename:
            f = open(filename, 'r')
            contents = f.readlines()[1:]
            title = contents[0].strip()

            rawLine = []
            dataStamp = []
            val21 = []
            val22 = []
            tot = []
            
            # COUNT SAMPLES
            sampleCount = 0
            for line in contents:
                rawLine.append("0")
                dataStamp.append("0")
                val21.append("0")
                val22.append("0")
                tot.append("0")
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

            np.savetxt("output.csv", rawLine, delimiter=',')

            f.close()

    def print_file(self):
        f = open(self.open_file, "rw+")
        line = f.readline()
        print(line)

            
    def save_file(self):
        filename = fd.asksaveasfilename(filetypes=[("Plik tekstowy","*.txt")], defaultextension = "*.txt") # wywołanie okna dialogowego save file

apl = Application()