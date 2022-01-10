from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score = Scoreboard()
snake = Snake()
screen.listen()
food = Food()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True


def end_game():
    global game_is_on
    game_is_on = False


screen.onkey(end_game, "space")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.change_place()
        score.increase_score()
        snake.extend()

#     Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 15:
            score.reset()

screen.exitonclick()
