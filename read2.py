import tkinter as tk
from tkinter import filedialog as fd

import re

import numpy as np

class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.title("Notatnik")

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
        filename = fd.askopenfilename(filetypes=[("Plik tekstowy","*.txt")]) # wywołanie okna dialogowego open file
        
        if filename:
            print(filename)
            f = open(filename, 'r')
            contents = f.readlines()[1:]
            title = contents[0].strip()

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

            print(step2)
            f.close()

    def print_file(self):
        f = open(self.open_file, "rw+")
        line = f.readline()
        print(line)

            
    def save_file(self):
        filename = fd.asksaveasfilename(filetypes=[("Plik tekstowy","*.txt")], defaultextension = "*.txt") # wywołanie okna dialogowego save file

apl = Application()