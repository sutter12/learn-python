import turtle as t #https://docs.python.org/3/library/turtle.html

global dotList #List of tuples
square = [
    (-100, 100),
    (100, 100),
    (100, -100),
    (-100, -100)
]
star = [
    (-100, -10),
    (0,150),
    (100, -10),
    (-100, 90),
    (100, 90)
]

def setDots(shape):
    global dotList
    t.penup()

    for i in range(len(dotList)):
        t.goto(dotList[i])
        t.dot()
        t.write(str(i+1), move = False, align = 'left', font = ('Arial', 12, 'normal'))
    t.goto(dotList[0]) #goto starting point of drawing

def correctPos(x, y):
    global dotList
    tolerance = 20

    for i in range(len(dotList)):
        correctX = dotList[i][0]
        correctY = dotList[i][1]

        if x <= correctX + tolerance and x >= correctX-tolerance:
            x = correctX
        if y <= correctY + tolerance and y >= correctY-tolerance:
            y = correctY

    t.goto(x, y)

def click(x, y):
  correctPos(x, y)

dotList = square

t.hideturtle()

setDots(dotList)

t.speed(0)
t.pendown()

t.onscreenclick(click)

t.done()