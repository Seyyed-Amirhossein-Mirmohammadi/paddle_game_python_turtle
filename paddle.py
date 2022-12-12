import turtle
import random
import time

turtle.colormode(255)

def random_color(t):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    t.color(r,g,b)




def game_atm():
    w = turtle.Screen()
    w.title("paddle game")
    w.bgcolor("black")
    w.setup(550,700)
    w.tracer(0)
    return w


def paddle():
    p = turtle.Turtle()
    p.speed(0)
    p.shape("square")
    p.shapesize(0.5,3.5)
    p.color("blue")
    p.penup()
    p.goto(0,-260)
    p.direction = "ist"
    return p

def ball():
    b = turtle.Turtle()
    b.speed(0)
    b.shape("circle")
    b.color("red")
    b.penup()
    b.shapesize(0.5,0.5)
    b.goto(0,-245)
    return b

def targets():
    target = []
    for i in range(-4,5):
        for a in range(5,0,-1):
            targ = turtle.Turtle()
            targ.speed(0)
            targ.shape("square")
            targ.shapesize(1,1.5)
            random_color(targ)
            targ.penup()
            targ.goto(60*i-5,35*a+100)
            target.append(targ)
    return target

def ball_move():
    tup.setx(tup.xcor() + ball_vx)
    tup.sety(tup.ycor() + ball_vy)


def go_right():
    x = paddle.xcor()
    if x != 225:
        x = x + 5
        paddle.setx(x)
    
def go_left():
    x = paddle.xcor()
    if x != -225:
        x = x - 5
        paddle.setx(x)

def key_listenner(s):
    s.listen()
    s.onkeypress(go_right, "Right")
    s.onkeypress(go_left, "Left")


def vertical_wall_col():
    if tup.xcor() > 265:
        return True
    if tup.xcor() < -270:
        return True

def horizontal_wall_coll():
    if tup.ycor()>350:
        return True


def paddle_coll():
    if abs(tup.xcor()-paddle.xcor()) < 30 and tup.ycor()-paddle.ycor() <10 and tup.ycor() < -255:
        return True


def targets_coll():
    for i in hadaf:
        if i.distance(tup) < 20:
            i.goto(1000,1000)
            return True

def check_lose():
    if tup.ycor() < -300:
        return True


def clear_targets():
    for x in hadaf:
        x.goto(1000,1000)


def read_highscore():
    FILE = open("highscore.txt")
    hiighscore = FILE.readline()
    hiighscore = int(hiighscore)
    return hiighscore

def save_highscore():
    FILE = open("highscore.txt" , "w")
    high = str(high_score)
    FILE.write(high)
    FILE.close()


def score_writer():
    score_turtle.goto(-180,300)
    score_turtle.color("white")
    score_turtle.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    score_turtle.hideturtle()

def highscore_writer():
    highscore_turtle.goto(100,300)
    highscore_turtle.color("white")
    highscore_turtle.write("High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))
    highscore_turtle.hideturtle()


ball_vx = 2
ball_vy = 2
score_turtle = turtle.Turtle()
highscore_turtle = turtle.Turtle()
high_score = read_highscore()
score = 0
screen = game_atm()
tup = ball()
paddle = paddle()
hadaf = targets()
score_writer()
highscore_writer()

while True:
    ball_move()
    key_listenner(screen)

    if check_lose():
        clear_targets()
        hadaf = targets()
        if score > high_score:
            high_score = score
            highscore_turtle.reset()
            highscore_writer()
        save_highscore()
        score = 0
        time.sleep(0.5)
        tup.goto(0,-245)
        paddle.goto(0,-260)
        ball_vx = 2
        ball_vy = 2
        
    
    if targets_coll():
        ball_vy = ball_vy * -1
        score = score + 10
        score_turtle.reset()
        score_writer()


    if paddle_coll():
        ball_vy = ball_vy * -1

    if horizontal_wall_coll():
        ball_vy = ball_vy *-1

    if vertical_wall_col():
        ball_vx = ball_vx * -1



    screen.update()


