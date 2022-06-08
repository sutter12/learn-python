import turtle as t

global dotList #List of tuples
square = [
    (100, 100),
    (100, -100),
    (-100, -100),
    (-100, 100)
]
star = [
    (0,150),
    (100, 90),
    (-100, 90),
    (100, -10),
    (-100, -10)
]

def setDots(shape):
    global dotList
    t.penup()

    for i in range(len(dotList)):
        t.goto(dotList[i])
        t.stamp
        t.write(str(i))
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

setDots(dotList)

t.hideturtle()
t.speed(0)
t.pendown()

t.onscreenclick(click)

t.done()