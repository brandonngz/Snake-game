from turtle import Turtle, Screen
import time

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")

screen = Screen()
screen.tracer(0)


class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.score_counter = 0
        self.score()

    # Show "Score: " at the top of the game
    def score(self):
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.color('white')
        self.write(f"Score: {self.score_counter}", move=True, align=ALIGNMENT, font=FONT)
        time.sleep(0.1)
        screen.update()

    # Collision with the tail or wall, show message
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=True, align=ALIGNMENT, font=FONT)

    # Count +1 when the snake eat the food
    def score_increase(self):
        self.clear()
        self.score_counter += 1
        self.score()

