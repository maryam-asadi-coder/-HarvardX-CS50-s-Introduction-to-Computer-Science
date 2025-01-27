#This Python script is designed to manipulate CSV files. Specifically, it takes an input CSV file with columns named "name" and "house", splits the "name" column into "first" and "last" names, and writes the modified data to a new CSV file.
#.....
#This module provides functions for interacting with the Python interpreter.
#This module provides functions for reading and writing CSV files.
from sys import exit, argv
import csv #For reading and writing CSV files.

#Checks if the correct number of command-line arguments are provided (exactly two).
#Verifies that both arguments represent CSV files by checking their file extensions.
#The code ensures that exactly two command-line arguments are provided. These arguments represent the input and output CSV files. If the number of arguments is incorrect, the program exits with an error message.
if len(argv) < 3:
    exit("Too few command-line arguments")
elif len(argv) > 3:
    exit("Too many command-line arguments")
else:
    if argv[1][-4:] == ".csv" and argv[2][-4:] == ".csv":
        try:
            f = open(argv[1])
        except FileNotFoundError:
            exit(f"Could not read {argv[1]}")
        else:
            listofdict = []
            with f as file:
                reader = csv.DictReader(file)
                for row in reader:
                    x, y = row["name"].split(', ')
                    listofdict.append({"first": y, "last": x, "house": row["house"]})
            with open(argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for i in range(len(listofdict)):
                    writer.writerow({"first": listofdict[i]["first"], "last": listofdict[i]["last"], "house": listofdict[i]["house"]})
    else:
        exit("Not a CSV file")
#If the provided arguments are valid, the script opens the input CSV file.
#Using csv.DictReader, each row of the CSV file is read as a dictionary. Each dictionary represents a row in the CSV table, and the keys of the dictionary are the column names (like "name" and "house"), while the values are the data in those columns.
#For each row, the "name" column, which contains the full name, is split into "first" and "last" names.
#The new information (first name, last name, and house) is stored in a new dictionary, and this dictionary is added to a list.
