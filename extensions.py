
"""This code determines the MIME content type of a file based on its filename extension"""

#filename = input("Filename : ").lower().strip()
#This line prompts the user to enter a filename using the input function.
#The .lower() method converts the entire input to lowercase for case-insensitive matching.
#The .strip() method removes any leading or trailing whitespace characters from the filename
filename = input("Filename : ").lower().strip()
filename = '.'+filename.split('.')[-1]
#This line extracts the filename extension.
#It splits the filename string using the . (dot) as a delimiter, resulting in a list of components.
#The [-1] index accesses the last element of the list, which is the extension (e.g., ".txt", ".pdf").
# . is prepended using string concatenation to create a complete extension string (e.g., ".txt" becomes ".txt")
match filename:
    case ".gif":
        print("image/gif")
    case ".jpg" | ".jpeg":  #.jpg | .jpeg: This case uses a pattern matching operator (|) to handle both ".jpg" and ".jpeg" extensions, printing "image/jpeg" for both.
        print("image/jpeg") #Similar cases exist for ".png" (image/png), ".pdf" (application/pdf), ".txt" (text/plain), and ".zip"
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:  # This is a catch-all case using the underscore (_), which matches any extension not explicitly listed above. In this case, it prints "application/octet-stream", a generic content type for unknown binary files.
        print("application/octet-stream")
