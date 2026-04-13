# FB Financial Calculator P.2
from helpers import *
import threading

# COMPOUND INTEREST DOES NOT GIVE A READABLE DOLLAR AMOUNT----------------------------------------------------------------------------------

# Checks if it's valid, stolen from a past project

# Savings Time Calculator
    # Ask how much they want to save as a rounded FLOAT VAR
    # Ask how often they are putting in money (daily, biweekly, weekly, bimonthly, monthly, yearly)
        # check if it's valid
    # Ask how much money they are inserting
    # Divide the total they need by the total they amount they are adding
    # say that # is the amount of the time frames they need
    # optionally: convert time frame to every other time frame and present it in that form as well (e.g. Amount:100, inserting: 10, timeframe: monthly, "It will take ten months, or 40 weeks, or .83 years, or 80 biweeks, or ~300 days")
    # return to the menu

def savingstime(nwindow):

    savingstotal = roundfunc("How much do you want to have saved by the end?")
    savingamount = roundfunc("How much do you add each time you input money")
    print("You add money every:\n1.day\n2.week\n3.month\n4.year")
    timekeep = {1:"day", 2:"week", 3:"month", 4:"year"}
    timeframe = inputchecker(4)

    mintimes = round((savingstotal/savingamount), 2)

    print(f"It will take you {mintimes} {timekeep[timeframe]}s to save to {savingstotal:.2f}$")

    financemenu(nwindow)

# Compound Interest Calculator
    # Ask how much interest they have
    # Ask the amount of money they have
    # Ask how long they'll leave it alone
    # ask how often it compounds
    # convert interest into a percent (in decimal form)
    # make a loop that repeats the amount of time they'll leave it alone
        # every loop:
            # increase is money * interest
            # add increase to money
    # when loop ends, display info (e.g. "in # of time frame with interest, you will have #$")
    # return to menu func

def compoundinterest(nwindow):
            
    interest = roundfunc("What is your interest currently (out of 100, ex: 10'%' interest = 10 not .10)?")
    interest = interest/100
    startingamount = roundfunc("How much are you starting with?")
    timeamount = roundfunc("How long will you leave it alone?")
    timeamount = int(timeamount)

    for i in range(timeamount+1):
        startingamount = startingamount + (startingamount * interest)
    
    print(f"Your new amount of money will be {startingamount:.2f}$")

    financemenu(nwindow)

# Budget Allocator
    # ask how much money they have
    # ask how many categories they have
    # loop that many times with each time displaying "category #" (with number increasing by 1, starting at 1 every loop)
        # ask how what the category is
        # save it in a dictionary as a category:amount spent pair (which should be 0 at first)
    # ask how much they spend in each category (loop over each pair)
        # update every pair to the amount
    # add all the keys up (numbers) as a variable via loop
    # loop over the dictionary pairs:
        # inner function
            # divide the number by the total
            # multiply that by 100
            # display the new value with a % and the category name
    # call menu

def budget(nwindow):
    def percentageinator(total, amount):
        decimal = amount/total
        percent = decimal * 100
        return percent
    spent = 0
    money = roundfunc("What is your total amount of spendable money?")
    categoryamount = int(input("How many spending categories do you have?"))

    categoriesdict = {}
    numcount = 1
    for numcount in range(1, categoryamount+1):
        print(f"category {numcount}:")
        category = input("What is the name of this category?")
        categoriesdict.update({numcount:category})
        numcount += 1
    
    count = 0
    categoriespercents = {}
    for item in categoriesdict:
        count += 1
        print(f"{count}. {categoriesdict[count]}:")
        moneyspent = roundfunc("How much did you/will you spend in this category?")
        spent += moneyspent
        categoriespercents.update({count:percentageinator(money, moneyspent)})
    
    count = 0
    for item in categoriespercents:
        count += 1
        print(f"{categoriesdict[count]}: {categoriespercents[count]}%")
    
    if spent <= money:
        spentpercent = percentageinator(money, spent)
        print(f"You have {spent}$ left, or {spentpercent}% of your budget left.")
    else:
        print("You have went over your budget.")

    financemenu(nwindow)
        

# Sale Price Calculator
    # ask for the cost of an item
    # ask for the discount percent
    # subtract the discount from 100
    # divide that number by 100
    # multiply item cost by that number
    # display new cost

def salesprice(nwindow):
    cost = roundfunc("What is the cost of the item?")
    discount = roundfunc("What the discount? (out of 100, ex: 10'%' off discount = 10 not .10)")
    discount = discount/100

    newcost = -1 * ((cost*discount) - cost)
    print(f"The new cost is {newcost:.2f}")
    financemenu(nwindow)

# Tip Calculator 
    # ask for bill
    # ask for the tip percent
    # add the tip to 100 as a variable
    # divide that number by 100
    # multiply item cost by that number as a new cost variable
    # subtract old cost from new cost as a change variable
    # display new cost and change variable

def tipcalc(nwindow):
    bill = roundfunc("What is the order cost?")
    tip = roundfunc("How much are you tipping? (out of 100, ex: 10'%' off discount = 10 not .10)")
    tip = tip/100
    updbill = bill + (tip * bill)

    print(f"The new order cost is {updbill}")
    financemenu(nwindow)
# Menu func
    # Present the list of options (2-6)
    # Ask them which one they want to do
        # check if it's valid
    # call the corresponding function

def financemenu(nwindow):
    print("Which would you like to use?")

    optlist = ["1. Savings Time Calculator", "2. Compound Interest Calculator", "3. Budget Allocator", "4. Sale Price Calculator", "5. Tip Calculator", "6. Go back to menu"]

    for item in optlist:
        print(item)
    
    choice = inputchecker(6)

    if choice == 1:
        savingstime(nwindow)
    elif choice == 2:
        compoundinterest(nwindow)
    elif choice == 3:
        budget(nwindow)
    elif choice == 4:
        salesprice(nwindow)
    elif choice == 5:
        tipcalc(nwindow)
    elif choice == 6:
        print("(If this doesn't automatically open the window, you can also use the task bar)")
        nwindow.after(0, lambda: getwindow(nwindow))
        return
    
def financemenustartup(nwindow):
    thread = threading.Thread(
        target=financemenu,
        args=(nwindow,),
        daemon=True
    )
    thread.start()

# Startup function for FINANCE:
    # create a new thread using threading library
        # make the target function the financemenu
        # set the args to be the nwindow
        # set daemon to True
    # start the thread