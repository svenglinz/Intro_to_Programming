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
import re
import io

#Definition of functions
#########################################################################

#store path and separator as defined by user

while True:
    try:
        path = input("Please insert the path to the data file you want to input here:")

        # if the path contains windows backslashes this must be replaced
        if path.__contains__("\\"):
            path = path.replace("\\", "/")

        #if path is copied from file explorer in windoes, quotes are wraped around which must be eliminated
        if path.__contains__("\""):
            path = path.replace("\"", "")

        #loop which stores the data in the data frame if all inputs are valid. If errors occur,
        #user is asked to change his input

        #the original file should not be altered
        fin = open(path, "rt")
        data = fin.read()
        fin.close()
        data = re.sub(r"([A-Z])", r" \1", data)
        data = io.StringIO(data)
        bestsellers = pd.read_csv(data, sep="\t")
        bestsellers.columns = ["Title", "Author", "Date", "Year", "Type"]
        bestsellers["Year"] = bestsellers["Year"].astype("datetime64")
        print("Thanks. Your data has been imported sucessfully")
        break

    except FileNotFoundError:
        print("whoops. Something seems to have gone wrong. \n"
              "Please make sure that your input path is correct")
        path = input("path:")

#index is a vector of T/F which indicates which rows from the Data Frame Bestsellers should be chosen for display
def display_titles(index):
    output = bestsellers.loc[index]
    output.index = range(output.__len__())
    for i in range(output.__len__()):
        row = output.loc[i]
        print(row["Title"] + ", " + "by " + row["Author"] + " " + row["Year"].strftime("%d/%m/%Y"))

def input_integer(text):
    arg = input(text)
    while True:
        try:
            arg = int(arg)
            if int(arg) == float(arg):
                return(arg)
                break
            else:
                print("Please make sure to input a valid integer number")
        except ValueError:
            print("Please make sure to input a valid integer number")
            arg = input()

#function to display all books within a certain range of years (from start to end!)
def function1():
    while True:
        start = input_integer("Select start year:")
        end = input_integer("Select end year:")

        if end < start:
            print("Please make sure that your start value is before your end value")
            pass
        else:
            break

    start_date = bestsellers["Year"].dt.year >= start
    end_date = bestsellers["Year"].dt.year <= end
    range_dates = start_date & end_date

    if bestsellers.loc[range_dates].empty:
        print("No titles were found within the specified range of years")
    else:
        print("All Titles between" + " " + str(start) + " " + "and"+ " " + str(end) + ":")
        display_titles(range_dates)

#function to display all books in a specific month and year
def function2():

        month = input_integer("Select month")
        year = input_integer("Select year:")

        index_month = bestsellers["Year"].dt.month == month
        index_year = bestsellers["Year"].dt.year == year
        range = index_year & index_month

        display_titles(range)

#function to search for author
def function3():

    #input stuff & convert input to all lower cases
    user_input = input("Select")
    author = bestsellers["Author"].str.lower()
    index = title.str.contains(user_input)
    display_titles(index)

#function to search for a title
def function4():
    user_input = input("Select")
    #input stuff & convert input to all lower cases
    title = bestsellers["Title"].str.lower()
    index = title.str.contains(user_input)
    display_titles(index)

#execution of program
#########################################################################

#Function which asks the user for a file path and its separator.
#Based on the user input, the file is stored as a data frame under then name bestsellers

while True:
    selection = input("What would you like to do ? \n"
                      "1: Look up year range \n"
                      "2: Look up month/year \n"
                      "3: Search for author \n"
                      "4: Search for title \n"
                      "q: Quit\n")

    #user input is converted to integer if possible. If not, no conversion takes place
    try:
        selection = int(selection)
    except ValueError:
        pass

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
