"""
KIT101 2.1PP Turtle Graphics

Turtle Graphics task to draw the my First name's first letter and my Last name's first letter.
"""

__author__ = "ZUBAIR AHMED"

import turtle

def main():
    t = turtle.Turtle()
    t.speed(3)
    t.penup()
    t.forward(-150)
    t.pendown()
    
    # Drawing 'Z'
    t.pencolor("black")
    t.forward(50)  
    t.right(120)
    t.forward(100)
    t.left(120)
    t.forward(60)
    
    # Creating distance
    t.penup()
    t.forward(150)
    t.pendown()
    
    #Drawing 'A'
    t.left(120)
    t.forward(100) 
    t.left(120)
    t.forward(100) 
    t.forward(-50)
    t.left(120)
    t.forward(50)
    t.screen.mainloop()

if __name__ == "__main__":
      main()