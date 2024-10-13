"""
File : bookCatalogFinal.py
Author : Jeremy Martin
Last Modified : 10-12-24

The user is prompted to enter the application to add books to a text area output
adding the author first and last name as well as the book title. 

"""

from breezypythongui import EasyFrame

from tkinter import messagebox, PhotoImage
from tkinter.font import Font

class SplashScreen(EasyFrame):
    # Displays opening screen allowing the user to enter to add books or exit.

    # Initializes the window and widgets with format and text outputs.
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
    
        self.addRecordBtn = self.addButton(text = "Enter to Add Books", row = 5, column = 0, command = self.openAddBooks) # Opens second page where the user can enter author/title details.
        self.exitBtn = self.addButton(text = "Exit", row = 5, column = 2, command = lambda:quit()) # Exit button to close program if no entries are desired.

    def openAddBooks(self):
        self.destroy() # Destroys/closes the first window.
        AddBooks(self) # Opens the second window to add books.

class AddBooks(EasyFrame):
    """ Opens the second window where the user can add author/title details."""
    
    def __init__(self, master):
        """ Sets up the window and widgets. """
        EasyFrame.__init__(self, "Cozy Library Catalog - Add Books")
        self.setResizable(True)
        imageLabel = self.addLabel(text = "", row = 1, column = 1, columnspan = 2, sticky = "NSEW")
        textLabel = self.addLabel(text = "Welcome to the Cozy Library Catalog", row = 0, column = 1, columnspan = 2, sticky = "NSEW")

        # Load image and associate it with the image label
        self.image = PhotoImage(file = "cozyLibrary4.gif")
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
        self.outputArea = self.addTextArea("", row = 6, column = 0, columnspan = 3, width = 50, height = 5)

        self.addBookBtn = self.addButton(text = "Add Book", row = 5, column = 0, command = self.addBook)
        self.exitBtn = self.addButton(text = "Exit", row = 5, column = 2, command = lambda:quit())
        self.backBtn = self.addButton(text = "Back", row = 5, column = 1, command = self.goBack) # A button to allow the user to go back to the main page.

    def goBack(self):
        self.destroy() # Destroys/closes the current window in order to go back to the main page.
        SplashScreen() # Opens the main window again.


        

    def addBook(self): # Event handling method
        """Takes the user input for the required fields of author first name, author last name and book title."""
        # Obtain and validate the inputs
        authorFirstName = self.authorFirstName.getText()
        authorLastName = self.authorLastName.getText()
        bookTitle = self.bookTitle.getText()
        if not authorFirstName or not authorLastName or not bookTitle: # Error check to ensure all fields have input, else outputs an error message to let the user know.
            messagebox.showerror("Input Error", "All fields must be filled.")

        # Set the header for the table
        result = "%20s %20s %18s \n" % ("Author Last Name", "Author First Name", "Book Title")

        bookInfo = "%20s %20s %18s \n" % (authorLastName, authorFirstName, bookTitle)

        # Output the result while preserving the read-only status
        self.outputArea["state"] = "normal"
        self.outputArea.setText(result + "\n" + bookInfo)
        self.outputArea["state"] = "disabled"


"""
       This section was an early attempt for a prompter box for the error message. I couldn't get it to work properly so found the
       other method above with the tkinter messagebox function. 
      
    def errorPrompt(self):
        text = self.prompterBox(title = "Cannot have empty fields.", promptString = "Author First Name")
        self.label["text"] = "Author First Name"
  


class ErrorPrompt(EasyFrame):
    def __init__(self):
        # Sets up the window and widgets
        EasyFrame.__init__(self, title = "Error")
        self.addLabel = self.addLabel(text= "Cannot have empty fields.", row = 0, column = 0, sticky = "NSEW")
        self.addButton(text = "Return", row = 1, column = 0, command = AddBooks())
 
        # Set the header for the table
    result = "%18s %18s %18s \n" % ("Author Last Name", "Author First Name", "Book Title")
"""
        
        
def main():
    SplashScreen().mainloop()

if __name__ == "__main__":
    main()