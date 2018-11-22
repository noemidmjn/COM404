from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.x_image = PhotoImage(file="x.png")
        self.tick_image = PhotoImage(file="tick.png")

        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_title_label()
        self.add_name_label()
        self.add_passport_label()
        self.add_nights_label()
        self.add_checkin_button()
        self.add_name_entry()
        self.add_passport_entry()
        self.add_nights_entry()

        

        

    def add_title_label(self):
        self.title_label = Label()
        self.title_label.grid(row=0, column=1, columnspan=3)
        self.title_label.configure(font="Arial 24",
                                   text="Hotel Check In")

    def add_name_label(self):
        self.name_label = Label()
        self.name_label.grid(row=1, column=0, columnspan=2)
        self.name_label.configure(font="Arial 16",
                                  text="Name:")

    def add_passport_label(self):
        self.passport_label = Label()
        self.passport_label.grid(row=2, column=0, columnspan=2)
        self.passport_label.configure(font="Arial 16",
                                      text="Passport Number:")
        
    def add_nights_label(self):
        self.nights_label = Label()
        self.nights_label.grid(row=3, column=0, columnspan=2)
        self.nights_label.configure(font="Arial 16",
                                    text="No. of nights:")

    def add_checkin_button(self):
        self.checkin_button = Button()
        self.checkin_button.grid(row=4, column=1, columnspan=3)
        self.checkin_button.configure(font="Arial 20",
                                      text="Check In")

    def add_name_entry(self):
        self.name_entry = Entry()
        self.name_entry.grid(row=1, column=2, columnspan=2)

    def add_passport_entry(self):
        self.passport_entry = Entry()
        self.passport_entry.grid(row=2, column=2, columnspan=2)

    def add_nights_entry(self):
        self.nights_entry = Entry()
        self.nights_entry.grid(row=3, column=2, columnspan=2)

    def add_image_label(self):
        self.image_label = Label()
        self.image_label.grid(row=1, column=4, columnspan=1)
        self.image_label.configure(image=self.x_image,
                                   height=30,
                                   width=30)

    def add_image_label(self):
        self.image_label = Label()
        self.image_label.grid(row=2, column=4, columnspan=1)
        self.image_label.configure(image=self.x_image,
                                   height=30,
                                   width=30)

    def add_image_label(self):
        self.image_label = Label()
        self.image_label.grid(row=3, column=4, columnspan=1)
        self.image_label.configure(image=self.x_image,
                                   height=30,
                                   width=30)

    def checkin_button_clicked(self, event):
        if there is something in the box:
            self.image_label.configure(image=self.tick_image)

        else:
            self.image_label.configure(image=self.x_image)
        



# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
