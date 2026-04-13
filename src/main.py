import menu
import sys
import tkinter as tk
from helpers import *

def main():

    def leave():
        sys.exit()

    def openmenu():
        mainwindow.iconify()
        menu.mainmenu(mainwindow)
    # Go to the main menu (displays all of the important buttons and descriptions), minimize this window
    

    mainwindow = tk.Tk()
    mainwindow.title("Personal Portfolio")
    mainwindow.minsize(600, 200)
    mainwindow. maxsize(1920, 1080)
    mainwindow.geometry("600x200+750+100")

    # Create the mainwindow Tk object, make a title, min and max size, and original pop-up size

    start = tk.Label(mainwindow, text="Welcome to my personal portfolio!", font=("Sans Serif", 15, "italic"))
    contbtn = tk.Button(mainwindow, text="Continue to Menu", command=openmenu)
    exitbtn = tk.Button(mainwindow, text="EXIT program", command=leave)
    
    # Create a main title, a button to the main menu, and a exit program that shuts everything off

    desc = tk.Label(mainwindow, text="This is a personal portfolio program!\nIt includes four of the eleven personal project I made for my second semester of Computer Programming 2.\n(To navigate, press the buttons, which say what they do inside the button)\nPlease enjoy this simple showcase of some of my work so far!", border=5, relief="solid", width=70, height=5)
    
    # Create a label object that will hold the portfolio description

    contbtn.grid(row=2,column=1)
    exitbtn.grid(row=2,column=3)
    start.grid(row=0, column=1, padx=40, pady=10)
    # assign the locations of all the buttons and the title letters
    
    desc.grid(row=1, column=1, columnspan=3, rowspan=1)
    desc.configure(padx=50, pady=10)
    # assign the description box size and padding


    mainwindow.mainloop()

main()