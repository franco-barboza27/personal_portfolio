# FB CP2 Morse Code Translator
import sys as s
from helpers import *
import tkinter
import threading


# ALREADY GOOD, JUST NEEDS GUI------------------------------------------------------------------------------------------------------------
def translator(answerkey, sentence, conversion):

    printableform = []

    match conversion:
        case 0:
            becomesconversion = 1
        case 1:
            becomesconversion = 0

    try:
            for value in sentence:
                if value in answerkey[conversion]:
                    charindex = answerkey[conversion].index(value)
                    printableform.append(answerkey[becomesconversion][charindex])
    except:
        print("Oh! it looks like you didn't actually insert anything before pressing 0, huh...\n")
        morsethread(answerkey)

    displayer = ""

    for value in printableform:
        displayer = displayer + value

    return displayer

# for every character in the string
    # Check if the character is in the letters tuple
        # if it is, get its index
        # add the same index of the thing on the morse tuple to an empty string
        # if it isn't, add a space to the empty string

def wordstomorse(answerkey, nwindow):
    words = input("What would you like to encode into morse? (Please avoid non-alphabeticall or numerical values)\n")
    words = words.upper()

    displayer = translator(answerkey, words, 0)

    print(displayer)

    morsethread(answerkey, nwindow)

# Words to Morse translator
    # Tell them that the coder will not work with any special character aside from the space button

    # call the translator function

    # print the string
    # return to the main menu

def morsetowords(answerkey, nwindow):
    morsesentence = []

    while True:
        morse = input("What is the morse code of this character? (one letter or number in morse, no spaces, enter 0 to STOP inputting values and QUIT to go back to the menu):\n")
        if morse == "0":
            break
        elif morse == "QUIT":
            morsethread(answerkey, nwindow)
        else:
            morsesentence.append(morse)
        
        print("\n")
    
    displayer = translator(answerkey, morsesentence, 1)

    print(displayer)

    morsethread(answerkey, nwindow)
    

# Morse to Words
    # morse code string getter function
        # Looping
            # Ask for the morse code of one character they want to translate and add it to a list

        # while true
                # ask for morse code version of character

            # if the character is 0
                    # call the translator function with the list of indexes, and the two tuples
            # if the character is in the morse code tuple
                # add the character's index to a list


    # translator (morse to words)
        # try looping for every item in the list of indexes
            # a variable is equal to the character tuple at that at that index
            # append it to an empty string

        # display the finished up thing
        
def morsethread(answerkey, nwindow):
    print("1. Words to Morse\n2. Morse to Words\n3. Go back to the menu page\n")

    choice = inputchecker(3)

    match choice:
        case 1:
            wordstomorse(answerkey, nwindow)
        case 2:
            morsetowords(answerkey, nwindow)
        case 3:
            print("(If this doesn't automatically open the window, you can also use the task bar)")
            nwindow.after(0, lambda: getwindow(nwindow))
            return
# ask what they want to do, call the function

def morsemenustartup(answerkey, nwindow):
    thread = threading.Thread(
        target=morsethread,
        args=(answerkey, nwindow),
        daemon=True
    )
    thread.start()

# Startup function for MORSE TRANLATOR:
    # create a new thread using threading library
        # make the target function the morsethread
        # set the args to be the nwindow and the answerkey
        # set daemon to True
    # start the thread

def wordsandmorse():
    return [("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"), (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.")]
# Create a dictionary with a key for the MORSE tuple and a key for the letters tuple.