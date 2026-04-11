# FB 2nd Personal Library Program

import sys

# USES A SET, BUT IT JUST FUNCTIONS AS A STRING------------------------------------------------------------------------------------------

# input checking function
    # Loop until otherwise:
        # ask which item wanted
        # try to turn it into a number
            # if that doesn't work retry the loop
        # if it is in the range of the allowed inputs break the loop
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

# add item function
    # display What is the title of this book?  # In the future this can change to the word "work"
    # display Who is this book by?
    # if a book with the exact same information is in the library ask them to try a different book
    # otherwise add the book to the book database
    
    # call the menu
def additems(database):
    while True:
        name = input("What is the title of this book?:\n")
        creator = input("Who is the author of this book?:\n")

        database[0].append(name)
        database[1].append(creator)

        while True:
            print("Would you like to:\n1. Add another work\n2. Add a review\n3. Go to the menu")
            answer = inputchecker(3)

            if answer == 1:
                print("Very well")
                break
            elif answer == 2:
                review = input("What is your review of this work?:\n")
                updreview = f"Review of {name} by {creator}:\n{review}"
                database[2].add(updreview)
            else:
                print("Going to the menu")
                print("\n\n\n")
                menu(database)

# search for an item function
    # ask if they'd like to search by title or by author
    # if they choose author, ask which author
        # Display all books written by that author
    # if they chose title, ask what the title is
        # display the book and the author(s) who wrote it

    # call the menu
def searcher(database):
    print("Would you like to:\n1. Search by book name\n2. Search by author\n3. Go back to menu")
    checker = inputchecker(3)

    if checker == 1:
        booktitle = input("What is the name of the book? (Case sensitive):\n")
        counter = 0
        tracker = 0
        for item in database[0]:
            if item == booktitle:
                counter += 1
                print(f"{counter}. {item} by {database[1][tracker]}")
            tracker += 1
            
    elif checker == 2:
        authorname = input("What is the name of the author? (Case sensitive):\n")
        counter = 0
        tracker = 0
        for item in database[1]:
            if item == authorname:
                counter += 1
                print(f"{counter}. {database[0][tracker]} by {item}")
            tracker += 1
    
    print("\n\n\n")

# remove an item function
    # display What is the title of this book?  # In the future this can change to the word "work"
    # display Who is this book by?
    # if a book with the exact same information is in the library say that the book exists
        # Ask them if they really want to remove it
            # if they do, remove it 
            # if they don't, go back to the beggining of the remove item function
    # otherwise ask them to retry it

    # call the menu
def remover(database):
    title = input("What is the name of the book?")
    author = input("What is the name of the author?")

    print("Are you sure you want to remove all instances of this specific work from your database?\n1. Yes\n2. No")
    answer = inputchecker(2)
    if answer == 1:
        print("Now deleting and going to menu")
    else:
        print("Ok, going back to menu")
        menu(database)

    counter = 0
    for item in database[0]:
        if title == item:
            if database[1][counter] == author:
                database[0].pop(counter)
                database[1].pop(counter)
        counter += 1
    
    menu(database)
    print("\n\n\n")

# view works function
    # count = 1
    # get length of the database
    # for every pair in the booklist
        # display the count. book title and by author
        # add 1 to count
def viewworks(database):
    listednumber = 0
    databasesize = len(database[0])
    counter = 0

    while counter in range(0, databasesize):
        listednumber += 1
        print(f"{listednumber}. {database[0][counter]} by {database[1][counter]}")
        counter += 1
    print("\n\n")

    while True:
        print("Would you like to:")
        print("1. Go to menu\n2. Not yet")
        answer = inputchecker(2)

        if answer == 1:
            print("Going to the menu")
            menu(database)
            print("\n\n\n")
        elif answer == 2:
            print("Very well.")
        print("\n\n\n")

# View review function
    # Always looping until broken
        # Ask if they want to see a review
            # if they do, make an "item" = to a removed item from the review set
            # display the item
            # keep looping
    # otherwise go back to menu
def viewreviews(database):
    while True:
        print("Do you want to see a random review?\n1. Yes\n2. No")
        answer = inputchecker(2)

        if answer == 1:

            bufferreviewdata = set.copy(database[2])

            review = bufferreviewdata.pop()

            print(review)
        else:
            break
        print("\n\n\n")

# Menu function
    # Present the list of options (1-3)
    # Ask them which one they want to do
        # check if it's valid
    # call the corresponding function
def menu(database):
    while True:
        print("Which would you like to use? (enter the number of the item)")

        optlist = ["1. View booklist", "2. Search/sort", "3. Add a book", "4. Remove a book", "5. View reviews", "6. Exit"]

        for item in optlist:
            print(item)

        choice = inputchecker(5)
        print("\n\n\n")

        if choice == 1:
            print("Opening book list")
            viewworks(database)
        elif choice == 2:
            print("Opening sort menu")
            searcher(database)
        elif choice == 3:
            print("Going to the Item Addition menu")
            additems(database)
        elif choice == 4:
            print("Going to the Item Removal menu")
            remover(database)
        elif choice == 5:
            print("Opening the review menu")
            viewreviews(database)
        else:
            print("Are you certain you want to terminate the program? Doing so will permanantly clear your database.")
            print("1. Yes\n2. No")
            terminatequestion = inputchecker(2)
            if terminatequestion == 1:
                sys.exit()
            else:
                print("Very well, going back to the menu.")

print("Hello, this is a book database!\nThe main point of it is to store books and their authors inside of one library.")
books = [[], [], {"2/5 stars, mediocre."}]

menu(books)