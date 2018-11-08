from tkinter import *

class Gui(Tk):

    def __init__(self):

        # initialise the parent class (Tk)
        super().__init__()

        # set wintow attributes
        self.title("Newsletter")
        self.configure(height=500,
                       width=600)


        # add components/widgets
        self.add_heading_label()
        self.add_instruction_label()
        self.add_email_label()
        self.add_email_entry()
        self.add_subscribe_button()

        
    def add_heading_label(self):
        
        # 1. create the component
        self.heading_label = Label()
        self.heading_label.place(x=50, y=100)
        # 2. style the component
        self.heading_label.configure(font="Arial 24",
                                     text="RECEIVE OUR NEWSLETTER",
                                     )
        # 3. add event listeners to the component
        #todo


    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.place(x=50, y=200)
        self.instruction_label.configure(font="Arial 16",
                                         text="Please enter your email below to receive our newsletter.")


    def add_email_label(self):
        self.email_label = Label()
        self.email_label.place(x=60, y= 300)
        self.email_label.configure(font="Arial 16",
                                   text="Email:")

    def add_email_entry(self):
        self.email_entry = Entry()
        self.email_entry.place(x=125, y=305)


    def add_subscribe_button(self):
        self.subscribe_button = Button(text = "Subscribe")
        self.subscribe_button.place(x=20, y=400)
        self.subscribe_button.width(400)
