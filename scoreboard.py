from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 36, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.score = 0
        with open('data.txt') as file:
            self.high_score = file.read()
        # self.high_score = int(self.data_score)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High_Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('data.txt',mode='w') as file:
                file.write(str(self.score))
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update_score()


