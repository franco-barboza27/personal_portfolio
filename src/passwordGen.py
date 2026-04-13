# FB 2nd Password Generator
import random as r
import threading
from helpers import *

# COMPOUND INTEREST DOES NOT GIVE A READABLE DOLLAR AMOUNT----------------------------------------------------------------------------------
    # display the option list (1.generate a password, 2. exit program)

    # call the input checker

    # if they chose to generate
        # call the requirements function
    # if they chose to exit
        # leave the program
def passmenu(window):
    print("1. make a password\n2. leave the program?")
    placevar = inputchecker(2)

    match placevar:
        case 1:
            requirements(window)
        case 2:
            print("(If this doesn't automatically open the window, you can also use the task bar)")
            window.after(0, lambda: getwindow(window))
            return
        
def passmenustartup(window):
    thread = threading.Thread(
        target=passmenu,
        args=(window,),
        daemon=True
    )
    thread.start()

    # Startup function for PASSWORD GEN:
    # create a new thread using threading library
        # make the target function the passmenu
        # set the args to be the window
        # set daemon to True
    # start the thread



# requisite asker FUNCTION
    # always looping
        # ask for the length of the password

        # try turning it into an integer
            # if it works, break the loop
            # otherwise keep looping

    # for every item in given list
        # ask if they would like to do the item
            # add their answer as an item to a different list

    # call generator

def requirements(window):
    while True:
        try:
            passwordlength = int(input("How many characters should the password be?:\n"))
            break
        except:
            print("That is an invalid input, did you try a WHOLE NUMBER?")

    otherrequisites = ["capital letters?", "lowercase letters?", "numbers?", "special characters (Ex: '$!@' etc)?"]
    answerstorage = [passwordlength]
    
    for item in otherrequisites:
        while True:
            answer = input(f"Should it include {item}Y/N\n")
            match answer:
                case "Y":
                    answer = True
                    break
                case "N":
                    answer = False
                    break
                case _:
                    print("That was an invalid input, did you try Y or N?")
        
        answerstorage.append(answer)
    
    generator(answerstorage, window)


# generator FUNCTION
    # call requisite function
    
    # current length of password is 0

    # Helper generator FUNCTION
        # if the number is X (arbitrary number),
            # check the Xnd(the item with the index X) item in the requisites list is true
                # choose a random number in the range of the 1st number in the Xs key and the 2nd number (ex: key:[1st val, 2nd val])
                # add it to a list
        # return list

    # loop 4 times
        #   while the current length list is in the range of the first value in requisites
            # choose a random number between 1 and 4 (dictionary with # key and ASCII range value)
            # call the helper generator as variable
            
            # current length = variable^ length

        # for every item in the variable, turn it into the ASCII version of the number
            # add it to a string
        
        # display the string

def generator(requisites, window):
    chartype = {1:[65, 90], 2:[97, 122], 3:[48, 57], 4:[33, 47]}
    tracker = [1, 2, 3, 4]

    def helpergenerator(trackervar, ranges, requirements):
        while True: 
            currentchar = r.choice(trackervar)

            if requirements[currentchar] is True:
                asciirange = ranges[currentchar]

                character = r.randint(asciirange[0], asciirange[1])
            
            trackervar.remove(currentchar)
            try:
                return character, trackervar
            except:
                trackervar = [1, 2, 3, 4]

    passwordnum = 0
    
    while passwordnum < 4:
        password = []

        while len(password) < requisites[0]:
            if not tracker:
                tracker = [1, 2, 3, 4]

            character, trackingvalues = helpergenerator(tracker, chartype, requisites)
            password.append(character)
            tracker = trackingvalues

        newpassword = []

        for item in password:
            item = chr(item)
            newpassword.append(item)
        
        password.clear()
        password = newpassword

        stringpassword = ""
        for item in password:
            stringpassword = stringpassword + item
        
        passwordnum += 1
        print(f"{passwordnum}. {stringpassword}")

    passmenu(window)