from turtle import Turtle, Screen
import time

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self,):
        super().__init__()
        self.score_counter = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score()

    # Show "Score: " at the top of the game
    def score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.color('white')
        self.write(f"Score: {self.score_counter}  High Score: {self.high_score}", move=True, align=ALIGNMENT, font=FONT)
        time.sleep(0.1)

    # Update with a Scoreboard
    def reset(self):
        self.clear()
        if self.score_counter > int(self.high_score):
            with open("data.txt", mode="w") as data:
                data.write(str(self.score_counter))
        self.score_counter = 0
        self.__init__()

    # Count +1 when the snake eat the food
    def score_increase(self):
        self.score_counter += 1
        self.score()

