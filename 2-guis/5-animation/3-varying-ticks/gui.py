from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()

        # load resources
        self.ball_image = PhotoImage(file="ball.png")
        self.squirtle_image = PhotoImage(file="squirtle.png")
        self.pikachu_image = PhotoImage(file="pikachu.png")
        self.charmander_image = PhotoImage(file="charmander.png")
        self.squirtle2_image = PhotoImage(file="squirtle2.png")
        self.pikachu2_image = PhotoImage(file="pikachu2.png")
        self.charmander2_image = PhotoImage(file="charmander2.png")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes

        self.num_ticks = 0
        
        # ball image
        self.ball_x_pos = 0
        self.ball_y_pos = 0
        self.ball_x_change = 10
        self.ball_y_change = 0

        # squirtle image
        self.squirtle_x_pos = 80
        self.squirtle_y_pos = 0
        self.squirtle_x_change = 20
        self.squirtle_y_change = 0

        # pikachu image
        self.pikachu_x_pos = 80
        self.pikachu_y_pos = 100
        self.pikachu_x_change = 20
        self.pikachu_y_change = 0

        # charmander image
        self.charmander_x_pos = 80
        self.charmander_y_pos = 200
        self.charmander_x_change = 20
        self.charmander_y_change = 0


        # add components
        self.add_ball_image_label()
        self.add_squirtle_image_label()
        self.add_pikachu_image_label()
        self.add_charmander_image_label()
        

        # start the timer
        self.tick()
        

    # the timer tick function    
    def tick(self):

        self.num_ticks = self.num_ticks + 1
        
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        
        if (self.num_ticks % 4 == 0):
            self.squirtle_x_pos = self.squirtle_x_pos + self.squirtle_x_change
            self.squirtle_y_pos = self.squirtle_y_pos + self.squirtle_y_change
            self.squirtle_image_label.place(x=self.squirtle_x_pos,
                                            y=self.squirtle_y_pos)

        if (self.num_ticks % 1 == 0):
            self.pikachu_x_pos = self.pikachu_x_pos + self.pikachu_x_change
            self.pikachu_y_pos = self.pikachu_y_pos + self.pikachu_y_change
            self.pikachu_image_label.place(x=self.pikachu_x_pos,
                                           y=self.pikachu_y_pos)
            
        if (self.num_ticks % 5 == 0):
            self.charmander_x_pos = self.charmander_x_pos + self.charmander_x_change
            self.charmander_y_pos = self.charmander_y_pos + self.charmander_y_change
            self.charmander_image_label.place(x=self.charmander_x_pos,
                                           y=self.charmander_y_pos)


            self.num_ticks = 0
            
                # ball 
            # check if hit right side
            if (self.ball_x_pos >= 420):
                self.ball_x_change = -self.ball_x_change



            # check if hit left side
            if (self.ball_x_pos <= 0):
                self.ball_x_change = -self.ball_x_change




                # squirtle
            # check if hit right side
            if (self.squirtle_x_pos >= 420):
                self.squirtle_x_change = -self.squirtle_x_change
                self.squirtle_image_label.configure(image=self.squirtle_image)
                

            # check if hit left side
            if (self.squirtle_x_pos <= 0):
                self.squirtle_x_change = -self.squirtle_x_change
                self.squirtle_image_label.configure(image=self.squirtle2_image)

                
                # pikachu
            # check if hit left side
            if (self.pikachu_x_pos >= 420):
                self.pikachu_x_change = -self.pikachu_x_change
                self.pikachu_image_label.configure(image=self.pikachu_image)

            # check if hit left side
            if (self.pikachu_x_pos <= 0):
                self.pikachu_x_change = -self.pikachu_x_change
                self.pikachu_image_label.configure(image=self.pikachu2_image)


                # charmander
            # check if hit left side
            if (self.charmander_x_pos >= 420):
                self.charmander_x_change = -self.charmander_x_change
                self.charmander_image_label.configure(image=self.charmander_image)

            # check if hit left side
            if (self.charmander_x_pos <= 0):
                self.charmander_x_change = -self.charmander_x_change
                self.charmander_image_label.configure(image=self.charmander2_image)

        

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
        self.squirtle_image_label.configure(image=self.squirtle2_image)

    # pikachu image
    def add_pikachu_image_label(self):
        self.pikachu_image_label = Label()
        self.pikachu_image_label.place(x=self.pikachu_x_pos,
                                        y=self.pikachu_y_pos)
        self.pikachu_image_label.configure(image=self.pikachu2_image)

    # charmander image
    def add_charmander_image_label(self):
        self.charmander_image_label = Label()
        self.charmander_image_label.place(x=self.charmander_x_pos,
                                        y=self.charmander_y_pos)
        self.charmander_image_label.configure(image=self.charmander2_image)
    


    
# the object
if __name__ == "__main__":
    gui = AnimatedGui()
    gui.mainloop()
