import turtle

board = turtle.Screen()
board.title("Pong")
board.bgcolor("blue")
board.setup(width=800, height=600)
board.tracer(0)

scoreA = 0
scoreB = 0

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("white")
paddleA.penup()
paddleA.goto(-350, 0)

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("white")
paddleB.penup()
paddleB.goto(350, 0)

ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   |   Player B: 0", align="center", font=("Courier", 24, "normal"))

# Center line
line = turtle.Turtle()
line.penup()
line.goto(0, 300)
line.pendown()
line.color("white")
line.right(90)

for _ in range(30):
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()

def paddleAmovUp():
    y = paddleA.ycor()
    y = y + 20
    paddleA.sety(y)

def paddleAmovDown():
    y = paddleA.ycor()
    y = y - 20
    paddleA.sety(y)

def paddleBmovUp():
    y = paddleB.ycor()
    y = y + 20
    paddleB.sety(y)

def paddleBmovDown():
    y = paddleB.ycor()
    y = y - 20
    paddleB.sety(y)

board.listen()
board.onkeypress(paddleAmovUp, "w")
board.onkeypress(paddleAmovDown, "s")
board.onkeypress(paddleBmovUp, "Up")
board.onkeypress(paddleBmovDown, "Down")

while True:
    board.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        scoreA = scoreA + 1
        pen.clear()
        pen.write("Player A: {}   |   Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        scoreB = scoreB + 1
        pen.clear()
        pen.write("Player A: {}   |   Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddleB.ycor() + 40) and (
            ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx = ball.dx * -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddleA.ycor() + 40) and (
            ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-340)
        ball.dx = ball.dx * -1
