# Author: Alexander Sutter
# Created: 09/01/2024

# main.py

# Imports
import turtle as t

def square(sideLength):
    t.pendown()
    for side in range(4):
        t.forward(sideLength)
        t.right(90)
    t.penup()

def drawSquareGrid(size):
    startPos = (0,0)
    columnSize = 90
    t.penup
    t.goto(startPos)
    # for col in range(size):
        # for row in range(size + 1):
    t.pendown()
    t.forward(columnSize * size)
    t.penup()
    t.goto(startPos[0], t.ycor() - columnSize)

    t.pendown()
    t.forward(columnSize * size)
    t.penup()
    t.goto(startPos[0], t.ycor() - columnSize)
    
    t.pendown()
    t.forward(columnSize * size)
    t.penup()

    t.goto(startPos)
    t.right(90)
    
    t.pendown()
    t.forward(columnSize * size)
    t.penup()
    t.goto(t.xcor() + columnSize, startPos[1])
    
    t.pendown()
    t.forward(columnSize * size)
    t.penup()
    t.goto(t.xcor() + columnSize, startPos[1])
    
    t.pendown()
    t.forward(columnSize * size)
    t.penup()
    
    t.goto(startPos)
    t.left(90)

# t.speed(0)

# square(90)
drawSquareGrid(2)

# pos = (0,0)
# print (pos)
# print (pos[0])

# t.onscreenclick()

t.done()