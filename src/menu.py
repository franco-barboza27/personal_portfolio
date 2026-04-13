import tkinter as tk
import os
import morseTranslate, oldLibrary, passwordGen, financeProject
from helpers import *

def mainmenu(window):
    def osclear():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")

    # Check what operating system they are on to correctly clear the terminal
        
    check = 0
    def morse():
        runbtn['command'] = lambda: (nwindow.iconify(), osclear(), morseTranslate.morsemenustartup(morseTranslate.wordsandmorse, nwindow))
        desc['text'] = "This program is a Morse Code Translator. It can translate text to Morse code and Morse code to text.\n\n\nWhat I learned:\n        \u25CF How to manage unknown values and maintain data uniformity\n      \u25CF Basic error and user input handling\n        \u25CF How to use functions to organize code\n\nChallenge I overcame:\n        \u25CF Managing the user input and making sure it was in the correct format"
    # Create a button that runs the morse code project
    # Update the description to be the morse code description
    def library():
        runbtn['command'] = lambda:(nwindow.iconify(), osclear(), oldLibrary.librarymenustartup(oldLibrary.bookget, nwindow))
        desc['text'] = "This is a library storage projects. It allows you to temporarily store books and interact with them!\n\n\nWhat I gained:\n         \u25CF Experience with managing data and abstracting functions\n         \u25CF knowledge on how different kinds of complex data(sets, lists, tuples, etc) can be used\n\nChallenge along the way:\n        \u25CF Foolproofing data to always work with user inputs and maintaining formats"
    # Create a button that runs the LIBRARY project
    # Update the description to be the library description
    def password():
        runbtn['command'] = lambda:(nwindow.iconify(), osclear(), passwordGen.passmenustartup(nwindow))
        desc['text'] = "This is a simple password generator!\nIt can generate passwords and check the strength of them using 5 choosable attributes\n(numbers, capital and lowercase letters, length, special characters)\n\n\nWhat I learned\n         \u25CF How to use nested functions in code.\n         \u25CF Work with nested loops to create customizability\n\nChallenge in programming:\n       \u25CF Creating logic for the structure of the code while implementing nested functions"
    # Create a button that runs the password generaator project
    # Update the description to be the password generator description
    def finance():
        runbtn['command'] = lambda:(nwindow.iconify(), osclear(), financeProject.financemenustartup(nwindow))
        desc['text'] = "This is a finance calculator! It can do a variety of things like track budgetting, savings, prices, and tip amounts!\n\n\nWhat was learned:\n       \u25CF How to incorporate real processes (financing) into code projects\n\n Challenge overcome:\n      \u25CF Creating equations for money based operations."
    # Create a button that runs the finance tracking project
    # Update the description to be the finance tracker's description


    def back():
        nwindow.iconify()
        window.update()
        window.deiconify()
        # create  way for the old window to reappear without having to go to the task bar using .update()(to anti-error) and deiconify(to pull the page back up)

    try:
        if nwindow:
            getwindow(nwindow)
    except:
        nwindow = tk.Toplevel(window)
        nwindow.title("Main Menu")
        nwindow.geometry("810x700+750+100")
    
    # Check if the window exists, and if it doesn't creates it entirely
    

    menu = tk.Label(nwindow, text="This is the menu\nYou can select a program to view its description.")
    menu.grid(row=0, column=1, columnspan=3, rowspan=1)
    menu.grid_configure(padx=10, pady=20)

    # Add the window's title to the top

    morsebtn = tk.Button(nwindow, text="Morse Code Translator", command=morse)
    libbtn = tk.Button(nwindow, text="Library", command=library)
    passbtn = tk.Button(nwindow, text="Password Generator", command=password)
    financebtn = tk.Button(nwindow, text="Finance Tracker", command=finance)
    # create the four buttons that lead to the description and run button command

    runbtn = tk.Button(nwindow, text="Run Selected Program")
    runbtn.grid(row=5, column=2)
    # create the run button to run a selected project

    morsebtn.grid(row=2, column=1, padx=10, pady=10)
    libbtn.grid(row=3, column=1, padx=10, pady=10)
    passbtn.grid(row=2, column=3, padx=10, pady=10)
    financebtn.grid(row=3, column=3, padx=10, pady=10)
    # Move all of the buttons(morse, library, password, finance) to the top in a grid formation.

    desc = tk.Label(nwindow, text="This is where the description of the program will be shown when you click on a program's button.", border=5, relief="solid", width=100, height=20)
    desc.grid(row=4, column=1, columnspan=3, rowspan=1)
    desc.configure(padx=50, pady=10)
    # assign a placeholder description and create a border for the decription box.

    backbtn = tk.Button(nwindow, text="Back to Original Page", command=back)
    backbtn.grid(row=6, column=2)
    # Assign a back button that allows the user to go to the first page again