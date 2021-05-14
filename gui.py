import tkinter as tk
from tkinter import *
from playsound import playsound
import convert
import os

class Application(tk.Frame):
    global dir, files
    dir = os.chdir('audio/')
    files = os.listdir()

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = tk.Label(self,text = 'Convert YT videos to mp3 here.')
        self.lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        self.field = tk.Text(self,width=30,height=1)
        self.field.grid(row=2, column=0, padx=10,sticky=W)

        self.upload = tk.Button(self, text='To mp3', width=5, command=self.convert)
        self.upload.grid(row=3, column=0, padx=10,sticky=W)

        self.lbl1 = tk.Label(self, text='All audio files in the working directory will appear here.')
        self.lbl1.grid(row=4, column=0, padx=10,pady=5,sticky=W)

        self.list = tk.Listbox(self)
        for item in files:
            self.list.insert('end', item)
        self.list.bind(self,'<Double-Button-1>',self.play)
        self.list.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        self.play = tk.Button(self,text='Play selected',width=10,command=self.play)
        self.play.grid(row=6,column=0,padx=10,pady=10,sticky=W)

    def convert(self):
        print(self.field.get(1.0, 'end'))
        convert.convertYtVid(self.field.get(1.0, 'end'))

    def play(self):
        selection = self.list.curselection()
        value = self.list.get(selection[0])
        playsound(value)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tavern Minstrel')
    app = Application(master=root)
    root.mainloop()