import turtle
import time
import random
from tkinter import messagebox



speed = 0.10

screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.bgcolor('lightgreen')
screen.setup(width = 600,height = 600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,100)
head.direction = 'stop'


food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.penup()
food.goto(0 , 0)
food.shapesize(0.80 , 0.80)


tails = []
point = 0

read = turtle.Turtle()
read.speed(0)
read.shape('square')
read.color('white')
read.penup()
read.goto(0 , 260)
read.hideturtle()
read.write('POİNT: {}'.format(point), align = 'center', font=('Courier', 24, 'normal'))




def move():
    if head.direction == 'Up':
        y = head.ycor()
        head.sety(y+20)
    if head.direction == 'Down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'Right':
        x = head.xcor()
        head.setx(x+20)
    if head.direction == 'Left':
        x = head.xcor()
        head.setx(x-20)

def goUp():
    if head.direction != 'Down':
        head.direction = 'Up'


def goDown():
    if head.direction != 'Up':
        head.direction = 'Down'


def goRight():
    if head.direction != 'Left':
        head.direction = 'Right'


def goLeft():
    if head.direction != 'Right':
        head.direction = 'Left'



screen.listen()
screen.onkey(goUp, 'Up')
screen.onkey(goDown,'Down')
screen.onkey(goLeft,'Left')
screen.onkey(goRight,'Right')

while True:
    screen.update()
    if head.xcor() > 300 or head.xcor()< -300 or head.ycor() > 300 or head.ycor() < -300 :
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'
        messagebox.showinfo("END GAME","YOU LOSE")



        for tail in tails:
            tail.goto(1000,1000)


        tails = []
        point = 0
        read.clear()
        read.write('POİNT: {}'.format(point), align='center', font=('Courier', 24, 'normal'))
        speed = 0.10

    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x , y)

        point = point +  10
        read.clear()
        read.write('POİNT: {}'.format(point), align='center', font=('Courier', 24, 'normal'))

        speed = speed - 0.0005

        NewTails =turtle.Turtle()
        NewTails.speed(0)
        NewTails.shape('square')
        NewTails.color('white')
        NewTails.penup()
        tails.append(NewTails)

    for i in range(len(tails) -1, 0 , -1):
        x = tails[i-1].xcor()
        y = tails[i-1].ycor()
        tails[i].goto(x, y)

    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)

    move()
    for segment in tails:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            messagebox.showinfo("END GAME","YOU LOSE")

            for segment in tails:
                segment.goto(1000, 1000)
            tails = []
            point = 0
            read.clear()
            read.write('Puan: {}'.format(point), align='center', font=('Courier', 24, 'normal'))
            speed = 0.10
    time.sleep(speed)