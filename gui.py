import tkinter as tk
from tkinter import *
import convert

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Sound Player')
    app = Application(master=root)
    root.mainloop()