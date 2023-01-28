from turtle import Turtle

ALIGNMENT="center"
FONT=("Courier", 15, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        self.hideturtle()
        self.pu()
        self.goto(0,270)
        self.score_print()
    
    def score_print(self):
        str=f"Score: {self.score}"
        self.write(str,align=ALIGNMENT,font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)
    
    def update(self):
        self.score+=1
        self.clear()
        self.score_print()