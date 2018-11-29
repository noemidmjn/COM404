from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()

        # load resources
        self.ball_image = PhotoImage(file="ball.png")
        self.squirtle_image = PhotoImage(file="squirtle.png")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        
        # ball image
        self.ball_x_pos = 200
        self.ball_y_pos = 80
        self.ball_x_change = 10
        self.ball_y_change = 10

        # squirtle image
        self.squirtle_x_pos = 250
        self.squirtle_y_pos = 80
        self.squirtle_x_change = -10
        self.squirtle_y_change = -10


        # add components
        self.add_ball_image_label()
        self.add_squirtle_image_label()
        

        # start the timer
        self.tick()
        

    # the timer tick function    
    def tick(self):
        
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        
        self.squirtle_x_pos = self.squirtle_x_pos + self.squirtle_x_change
        self.squirtle_y_pos = self.squirtle_y_pos + self.squirtle_y_change
        self.squirtle_image_label.place(x=self.squirtle_x_pos,
                                        y=self.squirtle_y_pos)
        


        # ball 
        # check if hit right side
        if (self.ball_x_pos >= 420):
            self.ball_x_change = -self.ball_x_change

        # check if hit bottom
        if (self.ball_y_pos >= 420):
            self.ball_y_change = -self.ball_y_change

        # check if hit left side
        if (self.ball_x_pos <= 0):
            self.ball_x_change = -self.ball_x_change

        # check if hit top
        if (self.ball_y_pos <= 0):
            self.ball_y_change = -self.ball_y_change


        # squirtle
        # check if hit right side
        if (self.squirtle_x_pos >= 420):
            self.squirtle_x_change = -self.squirtle_x_change

        # check if hit bottom
        if (self.squirtle_y_pos >= 420):
            self.squirtle_y_change = -self.squirtle_y_change

        # check if hit left side
        if (self.squirtle_x_pos <= 0):
            self.squirtle_x_change = -self.squirtle_x_change

        # check if hit top
        if (self.squirtle_y_pos <= 0):
            self.squirtle_y_change = -self.squirtle_y_change
        

        self.after(100, self.tick)



    # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)

    # squirtle image
    def add_squirtle_image_label(self):
        self.squirtle_image_label = Label()
        self.squirtle_image_label.place(x=self.squirtle_x_pos,
                                        y=self.squirtle_y_pos)
        self.squirtle_image_label.configure(image=self.squirtle_image)


    
# the object
if __name__ == "__main__":
    gui = AnimatedGui()
    gui.mainloop()
