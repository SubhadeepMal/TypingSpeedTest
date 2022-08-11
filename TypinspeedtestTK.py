from logging import root
import tkinter as tk
import time
import threading
import random
from PIL import ImageTk, Image

class typingtest:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Typing Speed Test")
        self.root.geometry("900x900")
        self.texts= open(r"D:\New_Programming\typingtext.txt","r").read().split("\n")
        self.frame=tk.Frame(self.root)

        
        self.img = ImageTk.PhotoImage(Image.open(r"C:\Users\Subhadeep\Desktop\istockphoto-1184426485-170667a.jpg"))  
        self.l=tk.Label(self.frame, image=self.img)
        self.l.place(x=0, y=0)

        # bg= tk.PhotoImage( file = r"C:\Users\Subhadeep\Downloads\wp6688799-typing-wallpapers.jpg")
        # label1 = tk.Label( self.frame, image = bg)
        # label1.place(x = 0,y = 0)

        self.speed1=tk.Label(self.frame, text="Enter the below text: ", font=("Helvetica",16))
        self.speed1.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.sampleLabel=tk.Label(self.frame, text=random.choice(self.texts),font=("Helvetica",14))
        self.sampleLabel.grid(row=2,column=0, columnspan=2, padx=5, pady=5)
        
        self.InputEntry=tk.Entry(self.frame, width=40, font=("Helvetica",24))
        self.InputEntry.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        self.InputEntry.bind("<KeyPress>", self.start)

        self.speed=tk.Label(self.frame, text="Speed: \n0.00 CPS\n0.00 CPM", font=("Helvetica",18))
        self.speed.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        self.reset=tk.Button(self.frame, text="RESET", command=self.reset)
        self.reset.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter=0
        self.run=False

        self.root.mainloop()

    def start(self, event):
        if not self.run:
            if not event.keycode in [16,17,18]:
                self.run= True
                t= threading.Thread(target= self.time_stamp)
                t.start()
        if not self.sampleLabel.cget('text').startswith(self.InputEntry.get()):
            self.InputEntry.config(fg="red")
        else:
            self.InputEntry.config(fg="black")
        if self.InputEntry.get() == self.sampleLabel.cget('text')[:-1]:
            self.run= False
            self.InputEntry.config(fg='green')

    def time_stamp(self):
        while self.run:
            time.sleep(0.1)
            self.counter+= 0.1
            cps=len(self.InputEntry.get())/self.counter
            cpm= cps*60
            wps= len(self.InputEntry.get().split(" "))/self.counter
            wpm= wps*60
            self.speed.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n{wps:.2f} WPS\n{wpm:.2f} WPM" )

    def reset(self):
        self.run=False
        self.counter=0
        self.speed.config(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPS")
        self.sampleLabel.config(text=random.choice(self.texts))
        self.InputEntry.delete(0, tk.END)

typingtest()
