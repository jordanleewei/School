from turtle import *

screen = Screen()
snake = Turtle()

resetscreen()

playing = True

color('red', 'yellow')
bgcolor('black')
screensize(500,500)
screen.delay(5)
snake.speed(2)

#key bindings to move snake
screen.onkey(snake.setheading(90), "Up")
screen.onkey(snake.setheading(180), "Right")
screen.onkey(snake.setheading(270), "Down")
screen.onkey(snake.setheading(0), "a")
screen.listen()

def game():
    forward(1)    

while playing:
    game()

done()