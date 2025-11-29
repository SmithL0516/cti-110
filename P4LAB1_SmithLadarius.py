# Ladarius Smith
# 11/29/25
# P4LAB1
# use turtle and loops to draw a square and a triangle

# Import the Libary
import turtle

# Create the turtle window and drawing object
win = turtle.Screen ()
pen = turtle.Turtle ()
win.bgcolor("orange")


# Set turtle options
pen.pensize (5)
pen.pencolor ("blue")
pen.fillcolor ("purple")
pen.shape ("arrow")
pen.begin_fill ()

# Code to draw the shapes
for side in range (4) :
    pen.forward (100)
    pen.left (90)


# Move to the top of the square
pen.left (90)
pen.forward (100)
pen.right (90)


#while loop that executes 3 times
sides = 3

while sides > 0:
    pen.forward (100)
    pen.left (120)
    sides = sides - 1
pen.end_fill ()


# Wait for user to close window
win.mainloop ()