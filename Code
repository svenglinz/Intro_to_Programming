#########################################################################
#Task: # Program which lets the user import data from the NYT Bestseller list.
#        User can then perform inspection tasks such as search for title,
#        authors, books in certain periods etc.
#Date: xx.xx.2021
#Authors:
#########################################################################


#Setup
#########################################################################
import pandas as pd


#Definition of functions
#########################################################################

#Function which asks the user for a file path and its separator.
#Based on the user input, the file is stored as a data frame under then name bestsellers
def input_selection():

    #store path and separator as defined by user
    path = input("Please insert the path to the data file you want to input here:")
    sep = int(input("Which separator is used in your file? Tab (0), Comma (1), Semicolon (2), Pipe (3) or else (4)"))

    # if the path contains windows backslashes this must be replaced
    if path.__contains__("\\"):
        path = path.replace("\\", "/")
        print(path)

    seps = ["\t", ",", ";", "|"]

    #loop which stores the data in the data frame if all inputs are valid. If errors occur,
    #user is asked to change his input
    while True:
        if sep in range(5):

            if sep == 4:
                sep = input("Please type in the separator you used")

            try:
                bestsellers = pd.read_csv(path, sep = seps[sep])
                print("Thanks. Your data has been imported sucessfully")
                break
            except FileNotFoundError:
                print("whoops. Something seems to have gone wrong. \n"
                      "Please make sure that your input path is correct")
                path = input("path:")
            except:
                print("separator error, please try again")
                sep = input("separator = ")
        else:
            sep = input("Please select a valid choice:")

        #user can at any time quit program by typing "q"
        if sep == "q" or path == "q":
            print("Programm sucessfully quit")
            break

#function to display all books within a certain range of years (from start to end!)
def function1():
    print()

#function to display all books in a specific month and year
def function2():
    print()

#function to search for author
def function3():
    print()

#function to search for a title
def function4():
    print()


#execution of program
#########################################################################

input_selection()

while True:

    selection = input("What would you like to do ? \n"
                      "1: Look up year range \n"
                      "2: Look up month/year \n"
                      "3: Search for author \n"
                      "4: Search for title \n"
                      "q: Quit\n"
                      "5: Change data")

    #user input is converted to integer if possible. If not, no conversion takes place
    try:
        selection = int(selection)
    except ValueError:

    #calls respective function based on which action the user wants to execute
    if selection in range(5):
        if selection == 1:
            function1()
        elif selection == 2:
            function2()
        elif selection == 3:
            function3()
        else:
            function4()
    elif selection in ["q", "Q"]:
        print("Program sucessfully quit")
        break
    else:
        print("Invalid Input. Please try again")
