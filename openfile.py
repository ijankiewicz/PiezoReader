import tkinter as tk
from tkinter.filedialog import askopenfile

class App(object):

    def __init__(self):
        self.root = tk.Tk()

        # create a frmae for a text and a toolbar
        text_frame = tk.Frame(self.root, width=200, height=200)
        text_frame.pack(fill="both", expand=True)

        # ensure a consistent GUI size
        text_frame.grid_propagate(False)

        # implement strechability
        text_frame.grid_rowconfigure(0, weight=1)
        text_frame.columnconfigure(0, weight=1)

        #create a Text widget
        self.text = tk.Text(text_frame, borderwidth=3, relief = "sunken")
        self.text.config(font=("consolas", 12), undo = True, wrap = "word")
        self.text.grid(row = 0, column = 0, sticky = 'nsew', padx = 2, pady = 2)

        #create a scrollbar and associate it with txt
        scrollbar = tk.Scrollbar(text_frame, command = self.text.yview)
        scrollbar.grid(row = 0, column = 2, sticky = 'nsew')
        self.text['yscrollcommand'] = scrollbar.set

        button = tk.Button(self.root, text = 'Open', command = self.open_file)
        button.pack(pady = 10)

    def open_file(self):
        # file = askopenfile(mode = "r", initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
        content = self.text.get("1.0", tk.END).splitlines()
        print(content)


app = App()
app.root.mainloop()