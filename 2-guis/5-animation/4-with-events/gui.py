from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()

        # load resources
        self.pikachu_image = PhotoImage(file="pikachu.png")
        self.pikachu2_image = PhotoImage(file="pikachu2.png")
       

        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.num_ticks = 0


        # pikachu image
        self.pikachu_x_pos = 0
        self.pikachu_y_pos = 0
        self.pikachu_x_change = 15
        self.pikachu_y_change = 15

        # add components
        self.add_pikachu_image_label()

        # start the timer
        self.tick()
        

    # the timer tick function    
    def tick(self):



            self.pikachu_x_pos = self.pikachu_x_pos + self.pikachu_x_change
            self.pikachu_y_pos = self.pikachu_y_pos + self.pikachu_y_change
            self.pikachu_image_label.place(x=self.pikachu_x_pos,
                                           y=self.pikachu_y_pos)
            

                # pikachu
            # check if hit right side
            if (self.pikachu_x_pos >= 420):
                self.pikachu_x_change = -self.pikachu_x_change
                self.pikachu_image_label.configure(image=self.pikachu_image)

            # check if hit left side
            if (self.pikachu_x_pos <= 0):
                self.pikachu_x_change = -self.pikachu_x_change
                self.pikachu_image_label.configure(image=self.pikachu2_image)

            # check if hit bottom
            if (self.pikachu_y_pos >= 250):
                self.pikachu_y_change = -self.pikachu_x_change
                self.pikachu_image_label.configure(image=self.pikachu2_image)

            # check if hit top
            if (self.pikachu_y_pos <= 0):
                self.pikachu_y_change = -self.pikachu_x_change
                self.pikachu_image_label.configure(image=self.pikachu2_image)



            self.after(100, self.tick)

    # pikachu image
    def add_pikachu_image_label(self):
        self.pikachu_image_label = Label()
        self.pikachu_image_label.place(x=self.pikachu_x_pos,
                                        y=self.pikachu_y_pos)
        self.pikachu_image_label.configure(image=self.pikachu2_image)


    
# the object
if __name__ == "__main__":
    gui = AnimatedGui()
    gui.mainloop()
