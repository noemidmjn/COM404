
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

        self.add_email_frame()

        self.add_email_label()

        self.add_email_entry()

        self.add_subscribe_button()

        

        



        

    def add_heading_label(self):

        

        # 1. create the component

        self.heading_label = Label()

        self.heading_label.grid(row=0, column=0, columnspan=2)

        # 2. style the component

        self.heading_label.configure(font="Arial 24",

                                     text="RECEIVE OUR NEWSLETTER",

                                     )

        # 3. add event listeners to the component

        #todo





    def add_email_frame(self):

        self.email_frame = Frame()

        self.email_frame.pack()

        



    def add_instruction_label(self):

        self.instruction_label = Label()

        self.instruction_label.pack()

        self.instruction_label.configure(font="Arial 16",

                                         text="Please enter your email below to receive our newsletter.")





    def add_email_label(self):

        self.email_label = Label(self.email_frame)

        self.email_label.pack(side=LEFT)

        self.email_label.configure(font="Arial 16",

                                   text="Email:")



    def add_email_entry(self):

        self.email_entry = Entry(self.email_frame)

        self.email_entry.pack(side=RIGHT)



    def add_subscribe_button(self):

        self.subscribe_button = Button(font="Arial 16",

                                       text = "Subscribe")

        self.subscribe_button.pack( side = BOTTOM)
