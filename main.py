from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Class instances
screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Classes methods
food.random_food()
scoreboard.score()


# Screen
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)


# Turn x/y direction the Snake
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# Start the game.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # Screen updated every 0.1 seg
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food.pos()) < 15:
        food.random_food()
        snake.extend_snake()
        scoreboard.score_increase()

    # Detect collision with wall.
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.reset()
        snake.reset()

    # Detect Coil Collision after snake head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

