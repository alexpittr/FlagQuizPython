import random
import turtle
scn = turtle.Screen()
t = turtle.Turtle()

def gabon():
    t.fillcolor("green")
    t.begin_fill()
    for i in range(2):
         t.fd(150)
         t.rt(90)
         t.fd(30)
         t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(0,-30)
    t.pd()
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(0,-60)
    t.pd()
    t.fillcolor("CornflowerBlue")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu

def luxembourg():
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
         t.fd(150)
         t.rt(90)
         t.fd(30)
         t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(0,-30)
    t.pd()
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(0,-60)
    t.pd()
    t.fillcolor("DeepSkyBlue")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu

def hungary():
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
         t.fd(150)
         t.rt(90)
         t.fd(30)
         t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(0,-30)
    t.pd()
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(0,-60)
    t.pd()
    t.fillcolor("MediumSeaGreen")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu

def ivorycoast():
    t.fillcolor("orange")
    t.begin_fill()
    for i in range(2):
         t.fd(45)
         t.rt(90)
         t.fd(100)
         t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(45,0)
    t.pd()
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(45)
        t.rt(90)
        t.fd(100)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(90,0)
    t.pd()
    t.fillcolor("ForestGreen")
    t.begin_fill()
    for i in range(2):
        t.fd(45)
        t.rt(90)
        t.fd(100)
        t.rt(90)
    t.end_fill()
    t.pu

def ireland():
    t.fillcolor("green")
    t.begin_fill()
    for i in range(2):
         t.fd(45)
         t.rt(90)
         t.fd(100)
         t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(45,0)
    t.pd()
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(45)
        t.rt(90)
        t.fd(100)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(90,0)
    t.pd()
    t.fillcolor("DarkOrange")
    t.begin_fill()
    for i in range(2):
        t.fd(45)
        t.rt(90)
        t.fd(100)
        t.rt(90)
    t.end_fill()
    t.pu


flags = [gabon, luxembourg, hungary, ivorycoast, ireland]
life = 3
points = 0
t.speed(100)

while life > 0 and len(flags) > 0:
    t.reset()
    flag = random.choice(flags)
    flag()

    answer = input("Which country is this flag? ")

    if answer == flag.__name__:
        flags.remove(flag)
        print("Bravo")
        points += 1
        print("You have", points, "points")
    else:
        life -= 1
        print("False")

if points > 3 and life > 1 :
     print("win")
elif points < 1 and life < 1:
    print("loss")





turtle.exitonclick()
