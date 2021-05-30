#########################################################################
#Task: # Program which lets the user import data from the NYT Bestseller list.
#        User can then perform inspection tasks such as search for title,
#        authors, books in certain periods etc.
#Date: xx.xx.2021
#Authors:
    #- 1
    #- 2
    #- 3
    #- 4
#########################################################################


#Setup
#########################################################################
import pandas as pd
import re
import io

# Define functions
#########################################################################

#Asks user for file path, imports file and formats the data for further analysis
#returns the prepared and cleaned CSV

def import_csv():
    while True:
        try:
            path = input("Please insert the path to the data file you want to input here:")

            # if the path contains windows backslashes (\), thse must be replaced by /
            if path.__contains__("\\"):
                path = path.replace("\\", "/")

            #if path is copied from file explorer in Windows, quotes are wraped around which must be eliminated
            if path.__contains__("\""):
                path = path.replace("\"", "")

            #open the file in read mode
            fin = open(path, "rt")
            #store the file in the data variable
            data = fin.read()
            fin.close()

            #Separate all words before each capital letter (as proxy to separate words)
            #and store data in a format that can be read by pd.read_csv
            data = re.sub(r"([A-Z])", r" \1", data)
            data = io.StringIO(data)

            #read modified csv file, store as bestsellers and modity data types and colnames
            bestsellers = pd.read_csv(data, sep="\t")
            bestsellers.columns = ["Title", "Author", "Publisher", "Date", "Type"]
            bestsellers["Date"] = bestsellers["Date"].astype("datetime64")
            print("Thanks. Your data has been imported sucessfully")
            return(bestsellers)
            break

        except FileNotFoundError:
            print("whoops. Something seems to have gone wrong. \n"
                  "Please make sure that your input path is correct")

#returns the titles selected by the user (given by a T/F string) in a readable format
def display_titles(index):
    output = bestsellers.loc[index]
    output.index = range(output.__len__())
    for i in range(output.__len__()):
        row = output.loc[i]
        print(row["Title"] + ", " + "by " + row["Author"] + " " + row["Date"].strftime("%d/%m/%Y"))

#function which makes sure that the user enters an integer number
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

    #create T/F string which indicates which books are within the selected years
    start_date = bestsellers["Date"].dt.year >= start
    end_date = bestsellers["Date"].dt.year <= end
    range_dates = start_date & end_date

    #print results
    if bestsellers.loc[range_dates].empty:
        print("No titles were found within the specified range of years")
    else:
        print("All Titles between " + str(start) + " " + "and " + str(end) + ":")
        display_titles(range_dates)

#function to display all books in a specific month and year
def function2():
    while True:
        month = input_integer("Select month:")      
        if month > 12 or month < 1:
            print("Please enter a new valid month")
            pass
        else:
            break
    while True:
        year = input_integer("Select year:")     
        if year > 2013 or year < 1942:
            print("Please enter a new valid year")
            pass
        else:
            break
    #create T/F string which indicates which books match the selected month and year
    index_month = bestsellers["Date"].dt.month == month
    index_year = bestsellers["Date"].dt.year == year
    range = index_year & index_month

    #print results
    if bestsellers.loc[range].empty:
        print("No titles were found at the specified month and year")
    else:
        print("All Titles in " + str(month) + ", " + str(year) + ":")
        display_titles(range)

#function to search for author
def function3():

    #create T/F string which indicates which books match the author name
    user_input = input("Enter an author's name (or part of a name): ").lower()
    author = bestsellers["Author"].str.lower()
    index = author.str.contains(user_input)

    #print results
    if bestsellers.loc[index].empty:
        print("No titles with the desired author were found")
    else:
        print("All Titles with the Author name " + user_input + ":")
        display_titles(index)

#function to search for a title
def function4():

    #create T/F string which indicates which books match the author desired title
    user_input = input("Enter a title (or part of a title): ").lower()
    title = bestsellers["Title"].str.lower()
    index = title.str.contains(user_input)

    #print results
    if bestsellers.loc[index].empty:
        print("No books with the desired title were found")
    else:
        print("All Books with the Title " + user_input + ":")
        display_titles(index)

#execution of program
#########################################################################

#import user file
bestsellers = import_csv()

#infinite loop which presents the user with the available selections.
#Upon selection, the resepctive function is executed and user can chose a new task
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
    if selection in [1,2,3,4]:
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
