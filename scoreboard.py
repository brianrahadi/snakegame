from turtle import Turtle
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = -1
        self.goto(x=0, y=270)
        self.increment()

    def increment(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",  align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=FONT)


