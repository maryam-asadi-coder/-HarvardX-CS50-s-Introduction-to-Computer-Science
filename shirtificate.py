from fpdf import FPDF
#Imports the FPDF library, which is essential for creating PDF files.
#maryam_asadi
#Defines a class named generate to encapsulate the certificate generation process.
class generate():
    def __init__(self, name):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "B", 45)
        pdf.cell(0, 60, "CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", x=0, y=70)
        pdf.set_font_size(30)
        pdf.set_text_color(255,255,255)
        pdf.text(x=45, y=140, txt=f"{name} took CS50")
        pdf.output("shirtificate.pdf")
#Initializes the class with the user's name as an argument.
#Creates a new FPDF object.
#Adds a new page to the PDF document.
#Sets the font to Helvetica, bold, and size 45.
#Adds the title "CS50 Shirtificate" centered on the page.
#Inserts the image "shirtificate.png" at the specified coordinates.
#Sets the font size to 30.
#Sets the text color to white.
#Adds a text line with the user's name and the message "took CS50" at the specified coordinates.
#Outputs the PDF document as "shirtificate.pdf".
#name = input("Name: ")
#pdf = generate(name)

class generate():
    def __init__(self, name):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "B", 45)
        pdf.cell(0, 60, "CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", x=0, y=70)
        pdf.set_font_size(30)
        pdf.set_text_color(255,255,255)
        pdf.text(x=45, y=140, txt=f"{name} took CS50")
        pdf.output("shirtificate.pdf")

name = input("Name: ")
pdf = generate(name)
