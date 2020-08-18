import turtle
import time
import random


# Time delay
delay = 0.1

# Score
score = 0
high_score = 0

# setup screen
wn = turtle.Screen()
wn.title("Snake by Prince")
wn.bgcolor("green")
wn.setup(width=600, height=800)
wn.tracer()  # Turn off update on screen

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Segment of body
segment = []

# Pen (Scoring display)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Score : 0  High Score : 0", align="center", font=("Courier", 20, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction == "up"


def go_down():
    if head.direction != "up":
        head.direction == "down"


def go_left():
    if head.direction != "right":
        head.direction == "left"


def go_right():
    if head.direction != "left":
        head.direction == "right"


def move():
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


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()

    # Border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segment
        for seg in segment:
            seg.goto(1000, 1000)  # The purpose of this is i will position the segment off the screen

        # Clear the segment list
        segment = []

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high_score), align="center",
                  font=("Courier", 20, "normal"))

    # Check for a collision in food
    if head.distance(food) < 20:
        # Move a food to a random
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)

        # Shorten the delay
        delay -= 0.0001

        # When there is collision score will add 10
        score += 10

        # Scoring
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high_score), align="center",
                  font=("Courier", 20, "normal"))

    # Move the end segment first in reverse order
    for index in range(len(segment)-1, 0, -1):
        x = segment[index - 1].xcor()
        y = segment[index - 1].ycor()
        segment[index].goto(x, y)

    # Move the segment to where the head is
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)

    move()

    # Check for the head collision
    for seg in segment:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segment
            for segments in segment:
                segments.goto(1000, 1000)  # The purpose of this is i will position the segment off the screen

            # Clear the segment list
            segment = []

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score : {}  High Score : {}".format(score, high_score), align="center",
                      font=("Courier", 20, "normal"))

    time.sleep(delay)

wn.mainloop()
