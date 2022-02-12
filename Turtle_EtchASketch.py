# Author: Alexander Sutter
# Date: 8/20/2021
# Latest Revision: 2/11/2022

import turtle

screen = turtle.Screen()

move = 50 #steps
turn = 90 #degrees

def w():
  turtle.fd(move)
def a():
  turtle.lt(turn)
def s():
  turtle.bk(move)
def d():
  turtle.rt(turn)


screen.onkey(w, "Up")
screen.onkey(s, "Down")
screen.onkey(a, "Left")
screen.onkey(d, "Right")

screen.listen()
turtle.done()