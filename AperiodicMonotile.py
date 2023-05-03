import math
import turtle
import time

# so after messing around with turtle and drawing the geometric series, i found a video about making patterns with lsystems
# https://www.youtube.com/watch?v=f6ra024-ASY    Im gonna try to take this idea and make something similar in python 

# basically an Lsystem will recursivly iterate a string, like turn x into xxy  and turn y into yxy, and repeat
# x -> xxy -> xxyxxyyxy -> xxyxxyyxyxxyxxyyxyyxyxxyyxy, etc
# we'll do this with an alphabet we make and assign all the characters to a turtles function, and each iteration will follow the instructions represented by our new string
# once we have this all working itll be as easy as swapping some numbers around to make lots and lots of fractals
# btw a fractal is in essence a recurssive shape, so while there are many famous patterns we can try to make, theres probably lots of interesting ones with no name
savedPos = []
posMark = (-1)





def lSystem(iter8s, ax, condition):
    seed = ax
    if iter8s == 0:
        return ax
    germSeed = ""
    for _ in range(iter8s):
        germSeed = "".join(condition[i] if i in condition else i for i in seed)
        seed = germSeed
    return germSeed
    
    

def savePos():
    x = turtle.xcor()
    y = turtle.ycor()
    h = turtle.heading()
    position = [x,y,h]
    savedPos.append(position)
    posMark = posMark + 1

def moveNoDraw(moveDist):
    turtle.penup()
    turtle.forward(moveDist)
    turtle.pendown
    

#alphabet
def lSysTransl8(shape, sys, angle, moveDist):
    #time.sleep(3)
    i = 0
    for ex in sys:
        if ex == 'L':
            turtle.left(angle)
        elif ex == 'R':
            turtle.right(angle)
        elif ex == 'D':
            turtle.forward(moveDist)
        elif ex == 'F':
            moveNoDraw(moveDist)
        elif ex == 'E': # special move for aperiodic monotile
            turtle.forward(math.sqrt(3)*25) # ONLY *50 TO FIT SCREEN, FOR PRETTY NUMBERS USE 100

def main(iter8s, ax, condition, angle, dist):
    
    sys = lSystem(iter8s, ax, condition) #iter8s, ax, condition
    shape = turtle.Turtle()
    sc = turtle.Screen()
    sc.setup(450, 450)

    turtle.up()
    turtle.backward(0)
    turtle.left(90)
    turtle.backward(0)
    turtle.left(0)
    turtle.down()
    turtle.penup()
    turtle.setpos(-250,0)
    turtle.pendown()
    turtle.speed(0)
    turtle.pensize(2)
    shape.hideturtle

    lSysTransl8(shape, sys, angle, dist)


einsteinTile = 0




if einsteinTile == 0:
                            #           ~~    MIGHT BE WRONG HERE
 #  ax = "DLLDRRRERRELLLDRDRRRERRELLLDRRDDRRDRRRELLERR"
  #  ax = "ERRRDLLDRRRERRELLLDRRDRRRERRELLLDRRDDRRDRRRELL"   def not THE aperiodic monotile, but close? found LOGO turtle script on github, said the E move im looking for was a*tan(60) but its not the hat
    ax = "RRRDLLDRRRERRELLLDRRDRRRERRELLLDRRDDRRDRRRELLE"
    condition = {"D":"DLLDRRRERRELLLDRRDRRRERRELLLDRRDDLLDRRRELLE"}
    iter8s = 0
    angle = 30
    dist = (1*50) # ONLY *50 TO FIT SCREEN, FOR PRETTY NUMBERS USE 100


main(iter8s, ax, condition, angle, dist)
turtle.mainloop()