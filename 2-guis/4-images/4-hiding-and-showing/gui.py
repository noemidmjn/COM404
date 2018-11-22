from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.map_image = PhotoImage(file="map.png")
        self.bus_image = PhotoImage(file="bus.png")

        

        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_title_label()
        self.add_name_label()
        self.add_passport_label()

        

    def add_title_label(self):
        self.title_label = Label()
        self.title_label.grid(row=0, column=1, columnspan=3)
        self.title_label.configure(font="Arial 24",
                                   text="Hotel Check In")

    def add_name_label(self):
        self.name_label = Label()
        self.name_label.grid(row=1, column=1, columnspan=2)
        self.name_label.configure(font="Arial 16",
                                  text="Name:")

    def add_passport_label(self):
        self.passport_label = Label()
        self.passport_label.grid(row=2, column=1, columnspan=2)
        self.passport_label.configure(font="Arial 16",
                                      text="Passport Number:")





 


# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
