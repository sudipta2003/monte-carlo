import matplotlib as mp
from matplotlib import pyplot as plt
import turtle as tu
import random as rd
from threading import Thread

screen = tu.Screen()
screen.screensize(canvheight=600,canvwidth=800)
screen.bgcolor("white")

#draw a square
square = tu.Turtle('square', visible=False)
def draw_square():
    square.shapesize(7,7)
    square.penup()
    square.setposition(x=-150,y=50)
    square.color("black", "red")
    square.pendown()
    square.showturtle()
    
    

#draw circle
circle = tu.Turtle('circle',visible=False)
def draw_circle():
    circle.shapesize(14)
    circle.color("black", "red")
    circle.penup()
    circle.setposition(x=200,y=50)
    circle.showturtle()
    



#put randowm dots
dot = tu.Turtle("circle", visible=False)
dot.color("black","yellow")
def put_dots(num):
    global s
    s = 1
    global c
    c = 0
    dot.shapesize(1)
    dot.speed(10)
    for i in range(num):
        dot.penup()
        x = rd.randint(-400,400)
        y = rd.randint(-300,300)
        dot.setposition(x,y)
        dot.pendown()
        dot.dot(10)
        screen.title("monte carlo simulation," + " status: " + str(i))
        dot.showturtle()
        if abs(dot.xcor() - square.xcor()) < 70 and abs(dot.ycor() - square.ycor()) < 70:
            s = s + 1
        if abs(dot.xcor() - circle.xcor()) < 120 and abs(dot.ycor() - circle.ycor()) < 120:    
            c = c + 1
        
        ratio = c/s
        y_axis.append(ratio)
        x_axis.append(i)
        plt.plot(x_axis,y_axis)

    dot.hideturtle()
    screen.title("monte carlo simulation" + " status: " + "done")


#run turtle
x_axis = []
y_axis = []
draw_square()
draw_circle()
put_dots(5000)
plt.ylabel('Ratio')
plt.xlabel('simulation')
plt.title('monte carlo Graph for PI')
plt.grid(True)
plt.show()


tu.done()