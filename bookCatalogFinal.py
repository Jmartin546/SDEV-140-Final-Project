"""
File : bookCatalogFinal.py
Author : Jeremy Martin
Last Modified : 10-12-24

The user is prompted to enter a generic temperature and have the program 
will have two buttons -- one to treat the input as Fahrenheit and convert 
it to Celsius; and one to treat the input as Celsius and convert it to Fahrenheit.

F = 9/5 * C + 32

F is the Fahrenheit temperature, and C is the Celsius temperature.

"""

from breezypythongui import EasyFrame

from tkinter import PhotoImage
from tkinter.font import Font

class SplashScreen(EasyFrame):
    # Displays splash screen
    def __init__(self):
        EasyFrame.__init__(self, "Cozy Library Catalog")
        self.setResizable(True)
        imageLabel = self.addLabel(text = "", row = 1, column = 1, sticky = "NSEW")
        textLabel = self.addLabel(text = "Welcome to the Cozy Library Catalog", row = 0, column = 1, columnspan = 3, sticky = "NSEW")

        # Load image and associate it with the image label
        self.image = PhotoImage(file = "cozyLibrary5.gif")
        imageLabel["image"] = self.image

        # Set font and color - this is for the caption
        font = Font(family = "Serif", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "black"
        textLabel["background"] = "brown"

        # Add labels and buttons to window
    
        self.addRecordBtn = self.addButton(text = "Enter to Add Books", row = 5, column = 0, command = self.openAddBooks)
        self.exitBtn = self.addButton(text = "Exit", row = 5, column = 2, command = lambda:quit())

    def openAddBooks(self):
        self.destroy()
        AddBooks(self)

class AddBooks(EasyFrame):
    """ Demonstrates a multiline text area. """
    
    def __init__(self, master):
        """ Sets up the window and widgets. """
        EasyFrame.__init__(self, "Cozy Library Catalog - Add Books")
        self.setResizable(True)
        imageLabel = self.addLabel(text = "", row = 1, column = 1, columnspan = 2, sticky = "NSEW")
        textLabel = self.addLabel(text = "Welcome to the Cozy Library Catalog", row = 0, column = 1, columnspan = 2, sticky = "NSEW")

        # Load image and associate it with the image label
        self.image = PhotoImage(file = "cozyLibrary6.gif")
        imageLabel["image"] = self.image

        # Set font and color - this is for the caption
        font = Font(family = "Serif", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "black"
        textLabel["background"] = "brown"

        self.addLabel(text = "Author First Name : ", row = 2, column = 1)
        self.addLabel(text = "Author Last Name : ", row = 3, column = 1)
        self.addLabel(text = "Book Title : ", row = 4, column = 1)
        self.authorFirstName = self.addTextField(text = "", row = 2, column = 2)
        self.authorLastName = self.addTextField(text = "", row = 3, column = 2)
        self.bookTitle = self.addTextField(text = "", row = 4, column = 2)
        self.outputArea = self.addTextArea("", row = 6, column = 0, columnspan = 3, width = 50, height = 20)

        self.addBookBtn = self.addButton(text = "Add Book", row = 5, column = 0, command = self.addBook)
        self.exitBtn = self.addButton(text = "Exit", row = 5, column = 2, command = lambda:quit())
        self.backBtn = self.addButton(text = "Back", row = 5, column = 1, command = self.goBack)

    def goBack(self):
        self.destroy()
        SplashScreen()

        

    def addBook(self): # Event handling method
        """Computes the investment schedule base on the inputs and outputs given. """
        # Obtain and validate the inputs
        authorFirstName = self.authorFirstName.getText()
        authorLastName = self.authorLastName.getText()
        bookTitle = self.bookTitle.getText()
        if not authorFirstName or not authorLastName or not bookTitle:
            print("Error")
            ErrorPrompt()
        
"""        
    def errorPrompt(self):
        text = self.prompterBox(title = "Cannot have empty fields.", promptString = "Author First Name")
        self.label["text"] = "Author First Name"
"""    


class ErrorPrompt(EasyFrame):
    def __init__(self):
        # Sets up the window and widgets
        EasyFrame.__init__(self, title = "Error")
        self.addLabel = self.addLabel(text= "Cannot have empty fields.", row = 0, column = 0, sticky = "NSEW")
        self.addButton(text = "Return", row = 1, column = 0, command = AddBooks())

"""

        
        
        
        # Set the header for the table
        result = "%4s %18s %10s %16s \n" % ("Author Last Name", "Author First Name", "Book Title")
        
        # Compute and append the results for each year
        totalInterest = 0.0
        for year in range(1, years + 1):
            interest = startBalance * rate
            endBalance = startBalance + interest
            result += "%4d %18.2f %10.2f %16.2f \n" % (year, startBalance, interest, endBalance)
            startBalance = endBalance
            totalInterest += interest

        # Append the totals for the period
        result += "Ending Balance: $%0.2f \n" % endBalance
        result += "Total interest earned: $%0.2f \n" % totalInterest

        # Output the result while preserving the read-only status
        self.outputArea["state"] = "normal"
        self.outputArea.setText(result)
        self.outputArea["state"] = "disabled"
        """
        
        
def main():
    SplashScreen().mainloop()

if __name__ == "__main__":
    main()
