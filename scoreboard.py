from turtle import Screen, Turtle

FONT = ("Courier", 25, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.goto((0, 260))
        self.color("white")
        self.penup()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align="center",
                   font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_board()

    def increase_score(self):
        self.score += 1
        self.update_board()


