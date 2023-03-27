from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

countdown = Scoreboard()
countdown.up()
countdown.speed("fastest")
countdown.color("white")


def odliczanie():
    countdown.goto(2, -12)
    countdown.write("3", align="center", font=("Courier", 15, "normal"))
    screen.update()
    time.sleep(1)
    countdown.clear()
    countdown.write("2", align="center", font=("Courier", 15, "normal"))
    screen.update()
    time.sleep(1)
    countdown.clear()
    countdown.write("1", align="center", font=("Courier", 15, "normal"))
    screen.update()
    time.sleep(1)
    countdown.clear()


snake = Snake()
food = Food()
food_2 = Food()
food_3 = Food()
napis = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
odliczanie()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        napis.score_up()

    if snake.head.distance(food_2) < 15:
        snake.extend()
        food_2.refresh()
        napis.score_up()

    if snake.head.distance(food_3) < 15:
        snake.extend()
        food_3.refresh()
        napis.score_up()

    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        game_is_on = False
        napis.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            segment.color("red")
            screen.update()
            game_is_on = False
            napis.game_over()


screen.exitonclick()
