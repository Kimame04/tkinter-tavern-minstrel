import shutil
import tkinter as tk
from tkinter import *
import simpleaudio as sa
import convert
import os

class Application(tk.Frame):
    global files

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = tk.Label(self,text = 'Convert YT videos to mp3 here.')
        self.lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        self.field = tk.Text(self,width=30,height=1,background='#d3d3d3')
        self.field.grid(row=2, column=0, padx=10,sticky=W)

        self.upload = tk.Button(self, text='To mp3', width=10, command=self.convert)
        self.upload.grid(row=3, column=0, padx=10,pady=5,sticky=W)

        self.refresh = tk.Button(self, text='Refresh', width=10, command=self.checkFiles)
        self.refresh.grid(row=3, column=0, padx=10,pady=5)

        self.lbl1 = tk.Label(self, text='All audio files in the working directory will appear here.')
        self.lbl1.grid(row=4, column=0, padx=10,pady=5,sticky=W)

        self.list = tk.Listbox(self)
        self.list.bind('<Double-Button-1>',self.play)
        self.list.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        self.checkFiles()

        #self.play = tk.Button(self,text='Play selected',width=10,command=self.play)
        #self.play.grid(row=6,column=0,padx=10,pady=10,sticky=W)

    def convert(self):
        print(self.field.get(1.0, 'end'))
        convert.convertYtVid(self.field.get(1.0, 'end'))
        self.checkFiles()

    def play(self,event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        wave_obj = sa.WaveObject.from_wave_file('audio/'+value)
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def checkFiles(self):
        files = os.listdir('audio/')
        if os.path.isfile('audio/.DS_Store'):
            os.remove('audio/.DS_Store')
        self.list.delete(0,END)
        for item in files:
            self.list.insert(END, item)
        if os.path.isdir('pytube/'):
            shutil.rmtree('pytube/')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tavern Minstrel')
    app = Application(master=root)
    root.mainloop()