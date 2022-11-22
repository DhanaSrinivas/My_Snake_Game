from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")



game_is_on = True

while game_is_on:
    screen.update()  # Here the snake is getting updated only after all the segments move.
    # T˳he screen updates only when this above line's encountered
    time.sleep(0.1)
    scorecard.update_score()
    snake.move()


    # Detecting collision with food
    if snake.head.distance(food) < 15:
        # print("nom nom nom")
        snake.extend()
        scorecard.increase_score()
        food.goto_random_position()

    if snake.head.xcor() >= 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() <= -290 :
        scorecard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            scorecard.reset()
            snake.reset()


screen.exitonclick()
