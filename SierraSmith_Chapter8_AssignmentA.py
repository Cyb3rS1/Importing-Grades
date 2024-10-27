# Grade Portal
# This program is dedicated for instructors who need to input three exam grades for each of
# their students. The first and last name, and all three exams of a student are recorded as a
# record into a CSV file. After all records are confirmed, the data can be read in tabular format.


DIV = "---" * 25

# module for organizing and displaying data in a table (tabular)
from texttable import Texttable

import time
import csv


# initial function that starts grade portal program
def main():


    # welcome message
    print("Welcome to the Grade Portal.")


    take_input()



# function that takes input (student data) and stores it into a list. The list gets passed
# to write_file() for writing the data into grades.csv
def take_input():


    # input that determines how many records will be made in the csv file
    how_many = int(input("How many students are you entering? "))

    print(DIV)

    # variable that compares to how_many when iterating through while loop
    count = 0

    # loading message
    print(f"Preparing entry fields for {how_many} students...\n")

    time.sleep(.5)

    # input format requirements and example
    print("Please enter the following data separated by commas.\n"
          "For example: First Name, Last Name, Exam1 score, Exam 2 score, Exam 3 score")

    print(DIV)

    # list where all student info will reside. The pre-entered strings are the headers
    # for a table that will display the student info.
    data = [["First name", "Last name", "Exam 1", "Exam 2", "Exam 3"]]

    # a while loop that iterates for each data entry until count == how_many
    while how_many > count:

        count += 1

        # input recorded for each student
        student = input(f"Student {count}:\n")

        # student data gets split by a comma delimiter, then assigned to info
        info = student.split(", ")

        # the newly formatted data is appended to the "data" list
        data.append(info)


    # after all student info has been recorded, transfer it to be written in the csv file
    write_file(data)



# function that writes data to grades.csv
def write_file(data):


    # open grades.csv for writing
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # write all rows of student info in the file at a time
        writer.writerows(data)

        # display success message
        print("\nGrade logging successful!\n")



# function that reads the csv file and displays its data in tabular format
def read_file():


    # where each row from grades.csv is stored before displaying them with Texttable()
    table = []

    # open the csv file for reading
    with open("grades.csv", 'r') as file:
        csvreader = csv.reader(file)

        # create an object for using the Texttable module
        t = Texttable()

        # append each row (including the header) to the "table" list
        for row in csvreader:

            table.append(row)

        # after all rows have been stored in "table" list, add the rows to the Texttable object
        t.add_rows(table)

        # display the student data using the Texttable object
        print(t.draw())



# call main() to start program
main()

# call separate read_file() function to read the csv file in tabular format
read_file()