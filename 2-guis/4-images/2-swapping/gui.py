from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.cacti_image = PhotoImage(file="cacti.png")
        self.cactiname_image = PhotoImage(file="cactiname.png")

        

        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_title_label()
        self.add_cacti_image_label()
        self.add_flip_button()

    def add_title_label(self):
        self.title_label = Label()
        self.title_label.grid(row=0, column=1, columnspan=2)
        self.title_label.configure(font="Arial 16",
                                   text="Cactus Leaves")

        
    def add_cacti_image_label(self):
        self.cacti_image_label = Label()
        self.cacti_image_label.grid(row=1, column=1, columnspan=2)
        self.cacti_image_label.configure(image=self.cacti_image,
                                             height=200,
                                             width=200)

    def add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=1, columnspan=2)
        self.flip_button.configure(font="Arial 16",
                                   text="Flip")

        self.flip_button.bind("<ButtonRelease-1>",
        self.left_button_clicked)
        
        self.flip_button.bind("<ButtonRelease-3>",
        self.right_button_clicked)

    def left_button_clicked(self, event):
         self.cacti_image_label.configure(image=self.cacti_image)

    def right_button_clicked(self, event):
        self.cacti_image_label.configure(image=self.cactiname_image)




 


# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
