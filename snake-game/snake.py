from turtle import Turtle, Screen
import time
from random import randrange

# Screen setup
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Snake setup
start_positions = [(0,0), (-20,0), (-40,0)]
segments = []

for position in start_positions:
    new = Turtle("square")
    new.up()
    new.color("white")
    new.goto(position)
    segments.append(new)
    
# Food
def generate_rand():
    new_location = (randrange(100), randrange(100))
    for segment in segments:
        if segment != new_location:
            return new_location
        else:
            return generate_rand()

def new_food():
    food_position = generate_rand()
    food = Turtle("circle")
    food.up()
    food.color("red")
    food.setposition(food_position)
    
# Check_collision

def check_collision(head, food):
    if head.distance(food) < 20:
        new_food()
    

# Movement of snake
playing = True

def move(segments):
    for i in range(len(segments) - 1, 0, -1):
        segments[i].setpos(segments[i-1].pos())
    segments[0].forward(20)
        
    
# Key bindings 
def up(): segments[0].setheading(90)
def down(): segments[0].setheading(270)
def left(): segments[0].setheading(180)
def right(): segments[0].setheading(0)
    
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.listen()





# Game loop
new_food()

while playing:
    screen.update()
    move(segments)
    time.sleep(0.1)



screen.exitonclick()