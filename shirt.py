#provides access to system parameters like command-line arguments
import sys
#provides functions for manipulating file paths
from os.path import splitext
#imports the Pillow library (a friendly fork of PIL) for image processing functionalities
from PIL import Image, ImageOps
#used for loading, manipulating, and saving images
#provides additional functionalities for image manipulation
import os
#Checks the number of command-line arguments:
#If less than 3 (input file and output file), it exits with an error message.
#If more than 3, it exits with an error message.
#Defines a list of valid output file extensions (e.g., .jpg, .jpeg, .png).
#Extracts the filename and extension of the input and output files from the arguments.
#Validates the output file extension:
#If the extension is not in the valid list, it exits with an error message.
#Checks if the input and output files have the same extension:
#If not, it exits with an error message.
#If all validations pass, it calls the edit_photo function with the input and output filenames.
def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        format = [".jpg", ".jpeg", ".png"]
        inp = os.path.splitext(sys.argv[1])
        outp = os.path.splitext(sys.argv[2])
        if outp[1].lower() not in format:
            sys.exit("Invalid output")
        elif inp[1].lower() != outp[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            edit_photo(sys.argv[1], sys.argv[2])

#Attempts to open a reference image named "shirt.png." This image will likely be used as a replacement for a portion of the input image.
#If the file is not found, it exits with an error message.
#Opens the input image using a context manager (with) for proper resource management.
#Resizes the input image to fit the size of the "shirt.png" image using ImageOps.fit.
#Pastes the resized input image onto the "shirt.png" image while respecting transparency areas using the mask argument.
#Saves the edited image to the specified output filename.
def edit_photo(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


if __name__ == "__main__":
    main()
#Overall, this program takes an image, resizes it to fit a reference image ("shirt.png"), and overlays it onto the reference image, potentially replacing a specific portion of the input image.
