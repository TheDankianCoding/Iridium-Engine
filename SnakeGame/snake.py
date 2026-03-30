
import turtle
import time
import random

rand = random.randint

#delay between moves
delay = 0.05

#score
score = 0
high_score = 0

#set up the screen
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) #turn off the screen updates

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("red")
food.penup()
food.goto(0, 100)
food.direction = "stop"

#score
Pen = turtle.Turtle()
Pen.speed(0)
Pen.shape("square")
Pen.color("white")
Pen.penup()
Pen.hideturtle()
Pen.goto(0, 260)
Pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

segments = []

#functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move(): #move the snake head in the direction it is currently moving And Be Moving About It Too (Movingly)
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#main game loop
while True:
    wn.update()

    #check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        #hide the segments
        for segment in segments:
            segment.goto(10000, 10000)
        #clear the segments list
        segments.clear()
        
        #Resetting Things
        #reset the score and the delay
        score = 0
        delay = 0.05
        Pen.clear()
        Pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #check for a collision with the food
    if head.distance(food) < 20:
        #move the food to a random spot
        x = rand(-280, 280)
        y = rand(-280, 280)
        food.goto(x, y)

        #Decrease the delay (Increase the Speed)
        delay -= 0.001

        #Score Handling
        score += 10
        if score > high_score:
            high_score = score

        Pen.clear()
        Pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("dark green")
        new_segment.penup()
        new_segment.color("dark green")
        segments.append(new_segment)

    #move the segments
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    #move the first segment to Right Behind where the head is
    if len(segments) > 0:
        if head.direction == "up":
            x = head.xcor()
            y = head.ycor()-20
            segments[0].goto(x, y)
        if head.direction == "down":
            x = head.xcor()
            y = head.ycor()+20
            segments[0].goto(x, y)
        if head.direction == "left":
            x = head.xcor()+20
            y = head.ycor()
            segments[0].goto(x, y)
        if head.direction == "right":
            x = head.xcor()-20
            y = head.ycor()
            segments[0].goto(x, y)
    
    #after One Tick, Move It Into Place Correctly (Moveingly)
    after_one_tick = time.time() + delay
    while time.time() < after_one_tick:
        wn.update()

    #Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 19:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            #hide the segments
            for segment in segments:
                segment.goto(10000, 10000)
            #clear the segments list
            segments.clear()

            #Resetting Things
            #reset the delay
            delay = 0.05

            #reset the score
            score = 0
            Pen.clear()
            Pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    move()

    time.sleep(delay)



wn.mainloop()