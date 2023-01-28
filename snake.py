from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_FORWARD=10
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
    
    def add_segment(self,posi):
        new_turtle=Turtle("square")
        new_turtle.color("white")
        new_turtle.pu()
        new_turtle.goto(posi)
        self.segments.append(new_turtle)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i-1].position())
        self.head.forward(MOVE_FORWARD)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(0)
