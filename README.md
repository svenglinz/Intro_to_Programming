## New York Times Best Sellers - Finder
- Language: Python 
- Group ID: 2303
- Group Members: Sven Glinz, Leopold Huberth, Nicolas Nipp and Mike Peruzzi
- Date: 30/05/2021

## Background and Objective:

**Background**: The New York Times Bestseller List is considered the most significant list of best-selling books in the United States. The rankings reflect sales figures that have been confidentially reported by sellers.Each week, thousands of different outlets report their actual sales of hundreds of thousands of individual titles. However, since the list is very comprehensive, it makes sense for readers to be able to sort books by their Favorite Authors and other criteria.

**Objective**: The goal of this program is to provide various search and filter options for a data set. The dataset refers to the New York Times bestseller list published since 1942 and filters by the 1# books on the list. The user should be enabled by the program to search the book list by various filters, such as author, year or title.

## Set-up
#### Required Programs and files:
1. **Python3**: The program was written with Python 3, so we can guarantee proper functionality only with the current version. Python is open source and thus available free of charge on the Internet and can be downloaded via the following [link](https://www.python.org/downloads/).

2. **Datafile**: The data used for the search functions is located in the bestseller2.txt file, which is provided above. This data set is a basic requirement for the use of the program, since all functions refer to it. The bestseller2.txt file contains information about the book title, author, publisher, category (fiction or non-fiction) and the date when the book was first ranked #1 on a bestseller list.

3. **Pandas**: Pandas is one of the most widely used python libraries in data science. It provides high-performance, easy to use structures and data analysis tools. Pandas makes it simple to do many of the time consuming, repetitive tasks associated with working with data. This program needs the package to sort out the data in the file and you can find a quick guide to download Pandas [here](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html).

4. **Regex**: A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern. This is required to allow the search functions to work. You can download the package [here](https://pypi.org/project/regex/).

## Program Description 
After all the necessary programs have been installed, there are several ways to start the search engine. The easiest way is to start Python directly and copy the code linked above into the console. After that, the user is asked for a file, which is again the bestseller2.txt. This can be downloaded directly from github and saved on your own computer. After that, only the path in the program must be linked and the preparations are complete.

The program gives you **4 options** to choose from, as well as the option to exit the program with "Q" or "q".

1.	**Display all books in a year range**:  Prompt the user for two years (a starting year and an ending year), then display all books which reached the #1 spot between those two years (inclusive).

2.	**Display all books in a specific month and year**:  Prompt the user to enter a month and year, then display all books which reached #1 during that month.

3.	**Search for an author**:  Prompt the user for a string, then display all books whose author’s name contains that string (regardless of case).

4.	**Search for a title**:  Prompt the user for a string, then display all books whose title contains that string (regardless of case).

## Sample Output
```
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
```
>1
```
Enter beginning year:
``` 
>1960
```
Enter ending year:
```
>1962
```
All Titles between 1960 and 1962 :
 A Shade of Difference, by Allen Drury (10/28/1962)
 Franny and Zooey, by J. D. Sallinger (10/29/1961)
 Hawaii, by James Michener (1/17/1960)
 Seven Days in May, by Fletcher Knebel (11/18/1962)
 Ship of Fools, by Katherine Anne Porter (4/29/1962)
 The Agony and the Ecstasy, by Irving Stone (4/23/1961)
 The Last of the Just, by André Schwarz-Bart (3/26/1961)
 Born Free, by Joy Adamson (8/7/1960)
 Calories Don't Count, by Herman Taller (3/25/1962)
 May This House Be Safe from Tigers, by Alexander King (3/13/1960)
 Silent Spring, by Rachel Carson (10/28/1962)
 The Making of the President - 1960, by Theodore H. White (9/10/1961)
 The New English Bible, by Oxford University Press (Editor) (5/28/1961)
 The Rise and Fall of the Third Reich, by William Shirer (12/4/1960)
 The Rothchilds, by Frederic Morton (6/24/1962)
 The Waste Makers, by Vance Packard (11/6/1960)
 Travels with Charley, by John Steinbeck (10/21/1962)
 ```
```
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
```
>2
```
Enter month (as a number, 1-12):
```
>9
```
Enter year:
```
>1990
```
All Titles in month 9 of 1990 :
 Four Past Midnight, by Stephen King (9/16/1990)
 Memories of Midnight, by Sidney Sheldon (9/2/1990)
 Darkness Visible, by William Styron (9/16/1990)
 Millie's Book, by Barbara Bush (9/30/1990)
 Trump: Surviving at the Top, by Donald Trump (9/9/1990)
 ```
```
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
```
>3
```
Enter an author's name (or part of a name):
```
>tolkein
```
All Titles with the Author name tolkein:
 Silmarillion, by J. R. R. Tolkein (10/2/1977)
 The Children of the Húrin, by J.R.R. Tolkein (5/6/2007)
 ```
```
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
```
>4
```
Enter a title (or part of a title):
```
>secret
```
All Books with the Title secret:
 Harry Potter and the Chamber of Secrets, by J. K. Rowling (6/20/1999)
 The Secret of Santa Vittoria, by Robert Crichton (11/20/1966)
 The Secret Pilgrim, by John le Carré (1/20/1991)
 ```


