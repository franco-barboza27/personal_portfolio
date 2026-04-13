import tkinter as tk

def inputchecker(rangeofchoices):
    while True:
            choicevar = input(f"Which one would you like to choose?(1~{rangeofchoices}):\n")
            try:
                choicevar = int(choicevar)
                if choicevar in range(1, rangeofchoices+1):
                    break
                else:
                    print("That's not an option :(")
                    continue
            except:
                    continue
            
    return choicevar

def roundfunc(question):
    while True:
        try:
            var = round(float(input(question)), 2)
            break
        except:
            print("You inputed a string of some kind (letters)")

    return var

def getwindow(window):
    print(f"Window state {window.state()}")

    window.deiconify()
    window.lift()
    window.focus_force()

    window.attributes('-topmost', True)
    window.after(100, lambda: window.attributes('-topmost', False))

    print(f"New state {window.state()}")