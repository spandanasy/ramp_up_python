# ramp_up_python
## Task 1 Python
1. Write a Python program for the following requirements.
2. Read a String statement from the command line
3. Findout total number of characters present in the statement.
4. Findout toal number of duplicate Characters in the statement
5. Findout total number of words present in the statement
6. Findout toal number of duplicate wordsin the statement
7. Reverse the characters present in the statement.
8. Reverse the words present in the statement.
9. Form a new statement from the reversed words.
10. Remove the duplicate characters from the latest statement.
11. Print final latest String statement.

* The input must be given through the console.
* To Find the length of the characters and words present in the statement len() and split() function is used.
* To Find the total number of duplicate words and characters dictionary is used so this gives a detailed view of the duplicate words and characters.
* To reverse a statement slice operation is performed which returns the reversed statement.
* To Remove the duplicate characters, nested for loops are used where the outer for loop iterates through words and the inner for loop iterates through characters
   of lists so this doesn't mess up the order of characters in the words.

## Task 2 Python
1. Write a Python program to validate the entered email address if the email is valid then write it into a file. Continue this operation until use says No/exit. 
2. If the user says Yes continue Validating emails and writing into the file
3. If the user says No then display all the email IDs from the file.
Note: Regex should be for validation

* The input is provided by the user to validate emails.
* To Implement this task Regular expressions and file operations are used.
* The re-module fullmatch () is used to get the full match of a required pattern, and all the validated emails will be stored in a text file created using file
   functions.
* After validating the prompt asks the user if they want to continue the process or have to exit if the user types ues the process will be continued and if the
  user says no then the valid emails will be printed from the file.

## Task 3 Python
1. Write a Python Program to check whether the entered IP is pining or not. Continue this operation until use says No/exit. 
2. Check whether the entered IP is valid or not with Regex.
3. If the IP is Pining write the IP into a txt file.
4. If the IP is not pining write the IP into a txt file.
5. If the user says Yes continue the IP validations and writing operations.
6. If the user Says No then stop checking the IPs and Print the Pinging IPs and Not pining IPs from the txt file
Note: Take a minimum of 10 IPs to test (Know IPs / Unknown IPs from Google)

* The input is provided by the user
* To implement this task modules like re, os, and ping3 are used.
* To install ping3 use command -->pip install ping3
* The IPs the user enters have to first be validated and if it's validated it should be pinged using the ping() function from the module ping3 if the ping is
  successful it should be addressed to a file and even if it's unsuccessful it should be added to file.
* Then a prompt asks a user to continue the process If yes the process continues if no the program is terminated while all the files get deleted.

## Task 4 Python
1. Write a Python Program to generate the employee details using the Random module.
* Employee Details: 
* Emp Id(1 to 9999) : Random Number
* Emp Location (Kormangala, HSR Layout, Ballary, Mumbai, Chennai, Nellore, Gurgaon, Hyderabad) Choose any city from the list dynamically
* Emp salary (20,000 to 1,50,000) Random Number.
2. Take Input from the command line for how many employee details to print and generate the employee details with the above-specified details.
3. DIsplay all the details using generators concepts, yield, next()

* The Input is given Through the command line to get the employee details of a specified number by the user
* The built-in modules random and locale are used to produce the employee details randomly and the locale is used to return the salary in the Indian number system.
* The special concept of generators is used to print the output of the randomized details, so this gives an enhanced feature of memory management.

## Task 5 python
### Write a Python program for Multiple Producers and Multiple Consumers using Threads 
   Take input from command line to set how many producers and consumers to perform functionality.

* This task is implemented using the concept of multithreading concept using consumer and producer concepts to show the process efficiently.
* Thread functions like start join and lock functions are used.

## Task 6 Python
### Calculate area of square, triangle and circle using both inheritance and function overloading, and use shape as base class.

* This task is implemented using the concept of Function overloading and Inheritance
* Function Overloading is the concept that contains a single function name but different varying parameter lengths.
* Inheritance is the concept where the child class acquires the properties of the parent class and implements them into their class.

## Task 7 Python
### An ATM machine returning 50, 200, 500 notes. Write a class-based (OOPs) program to print how many different types of notes the ATM machine will return? Validate if the user enter wrong amount for withdrawal.Print a valid message and ask either continue/cancel, with this perform your operations
* The Input of the amount is given by the user with positive integers if the input is having any blank space or any characters it should display a error message notifying the user the enter valid amount to return the count.
* Arithmatic operator like //(floor division) and %(modulus) are used to perform basic operations 
* dictionary is used to keep the count of notes.
* Notes that are in multiples of 50 are only provided to get the count of notes.

## Task 8 Python
### Write a Python Program for the following.
1. Create an excel/csv sheet manually with the following fields and fill the data as WFO / WFH / Blank Cell
2. Cell Headings: Emp ID, Aug 23, Aug 24, Aug 25, Aug 28, Aug 29, Aug 30
3. Fill the 10 employees data in the above cells. Check below image for reference
4. Findout how many employees marked WFH, WFO for today.
5. Findout how many employees marked WFH, WFO for the previous 5 days from the current date.
6. Findout employee id who has not filled the attendance in all today and previous 5 days..
7. Print the data like WFH & WFO Count on Current Date.

* using the pandas library a excel sheet data is loaded to perform manipulations.
* The datetime module is used to perform operartions on date for the specified query.
* some of the pandas functions like iterows(), isnull() are used to perfrom the blank entries and to iterratr through the row index. 

## Task 9 Python
### Please find the next task below and create a new excel sheet with the below table content for data and create a heat map as below:
1. Use the Python module 'https://plot.ly/python/heatmaps/' to achieve this.
2. the second column in Excel shows the size of the team and the blocks should be sized accordingly and the color should be based on what u specify in 3rd column. 3rd column can have precise RGB values as well.
3. The whole heat map should be rectangular.

* using plotly.express a rectangular gragh is created using the data loaded from excel sheet using pandas library.

## To Implement these task Python 3.11 or any latest versions can be used and any editors that support Python can be used.
