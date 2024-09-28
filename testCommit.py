"""
Class to display labels in quadrants
"""

from breezypythongui import EasyFrame

class LayoutDemo(EasyFrame):
    def __init__(self):
        # Sets up the window and the labels
        EasyFrame.__init__(self)
        self.addLabel(text = "(0,0)", row = 0, column =0, sticky = "NSEW") # Sticky anchors position with inputs N, S, E or W or any combination therein.
        self.addLabel(text = "(0,1)", row = 0, column = 1, sticky = "NSEW")
        self.addLabel(text = "(1,0 and 1)", row = 1, column = 0, sticky = "NSEW", columnspan = 2) # columnspan and rowspan merge cells
        #self.addLabel(text = "(1,1)", row = 1, column = 1, sticky = "NSEW")

def main():
    # Instantiates and pops up the window.
    LayoutDemo().mainloop()

if __name__ == "__main__":
    main()

"""
This is a test to show connection.
"""