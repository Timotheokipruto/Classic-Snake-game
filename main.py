from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


TIME_SLEEP = 0.20

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Classic Snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")


game_on=True

while game_on:
    screen.update()
    time.sleep(TIME_SLEEP)
    
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        if scoreboard.get_score()%5==0:
            TIME_SLEEP-=0.02
        

    #detect collision with wall
    if snake.head.xcor()>285 or snake.head.xcor()< -285 or  snake.head.ycor()>285 or snake.head.ycor()< -285:
        game_on=False
        scoreboard.game_over()


    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()






















screen.exitonclick()