from turtle import Screen
import time
from snake import Snake
from food import Food    
from scoreboard import Scoreboard
    
screen=Screen()
screen.setup(height=600,width=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(key="w",fun=snake.up)
screen.onkeypress(key="s",fun=snake.down)
screen.onkeypress(key="a",fun=snake.left)
screen.onkeypress(key="d",fun=snake.right)
    
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    
    #used to detect collision with food
    if snake.head.distance(food)<15:
        food.new_loc()
        scoreboard.update()
        snake.extend()
    
    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.ycor()<-280 or snake.head.xcor()<-280:
        game_is_on=False
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<5:
            game_is_on=False
            break
    
scoreboard.game_over()       





screen.exitonclick()