from sys import exit, argv #sys: This library provides access to system specific parameters and functions.
import csv #This library is used for reading and writing CSV (Comma-Separated Values) files.
import tabulate #This library (likely an external library that needs to be installed) is used to format the data from the CSV file into a table for printing.


if len(argv) < 2:
    exit("Too few command-line arguments")
elif len(argv) == 2:
    file_path = argv[1]
    #The script checks the number of arguments provided on the command line using len(sys.argv).
#If there are less than 2 arguments (including the script name itself), it exits with an error message indicating "Too few command-line arguments".
#If there are exactly 2 arguments, the second argument is assumed to be the file path and is stored in the file_path variable.
#Any other number of arguments triggers an exit with an error message indicating "Too many command-line arguments".
else:
    exit("Too many command-line arguments")
#The script checks if the provided file path ends with the ".csv" extension using string slicing (file_path[-4:]).
#If it's not a CSV file, it exits with an error message indicating "Not a CSV file".
if file_path[-4:] == ".csv":
    #If the file path is valid, it tries to open the file using open(file_path).
#If the file is not found, it catches a FileNotFoundError and exits with an error message indicating "File does not exist".
#If the file is opened successfully, it enters a with block which ensures the file is closed properly even if errors occur later.
#Inside the with block, a csv.reader object is created to read the contents of the CSV file.
#It iterates through each row in the CSV file using a for loop.
#For each row, it appends the row (which is a list of values) to a menu_list.
    try:
        f = open(file_path)
    except FileNotFoundError:
        exit("File does not exist")
    else:
        menu_list = []
        with f as file:
            reader = csv.reader(file)
            for row in reader:
                menu_list.append(row)
        print(tabulate.tabulate(menu_list, headers="firstrow", tablefmt="grid"))
        #After reading the entire file, the script uses the tabulate.tabulate function to format the menu_list (which contains all the CSV data) into a table.
#The headers="firstrow" argument specifies that the first row of the CSV file should be used as the table headers.
#The tablefmt="grid" argument (assuming it's from the tabulate library) likely specifies a grid-based table format for better presentation.
#Finally, the formatted table is printed using the print function.
else:
    exit("Not a CSV file")
    #In essence, this script provides a way to take a CSV file path as a command-line argument, read its contents, and display them in a user-friendly table format.
