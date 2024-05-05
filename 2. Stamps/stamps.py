"""
KIT101 3.2PP Stamp Function

Implements a reusable 'stamp' that can draw the author's initials at
any location on the Turtle Graphics window.
"""

__author__ = "ZUBAIR AHMED"

from turtle import Turtle

def place_stamp(stamper: Turtle, x: float, y: float, ink: str):
    """
    Draws the author's initials with the bottom-left corner of the drawing
    positioned at (x, y) and using the specified ink color.

    Parameters:
        stamper (Turtle): The turtle object.
        x (float): X-coordinate for the bottom-left corner of the drawing.
        y (float): Y-coordinate for the bottom-left corner of the drawing.
        ink (str): The color of the ink.
    """
    old_ink : str = stamper.pencolor()
    old_direction : float = stamper.heading()
    old_x : float = stamper.xcor()
    old_y : float = stamper.ycor()
    
    # offset = 50 
    stamper.pencolor(ink)
    stamper.penup()
    stamper.goto(x + 0, y + 86)  
    stamper.pendown()
    
    # Drawing 'Z'
    stamper.forward(50)
    stamper.right(120)
    stamper.forward(100)
    stamper.left(120)
    stamper.forward(60)
    
    # Creating distance
    stamper.penup()
    stamper.forward(150)
    stamper.pendown()
    
    # Drawing 'A'
    stamper.left(120)
    stamper.forward(100) 
    stamper.left(120)
    stamper.forward(100) 
    stamper.forward(-50)
    stamper.left(120)
    stamper.forward(50)
    
    stamper.penup()
    stamper.goto(old_x, old_y)
    stamper.pencolor(old_ink)
    stamper.setheading(old_direction)

def main():
    t = Turtle()  # The turtle graphics object

    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    # t.speed(0)

    # Call the place_stamp function with parameters
    place_stamp(t, 0, 0, "green")  
    place_stamp(t, -300, 0, "blue")       
    place_stamp(t, 250, 0, "red")
    
    # Avoid closing the window automatically
    t.screen.mainloop()

if __name__ == "__main__":
    main()
