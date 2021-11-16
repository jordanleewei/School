from turtle import Turtle, Screen, width
import time
from random import randrange

score = 0

# Screen setup
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
text = Turtle()
text.setpos(-300,-200)
text.hideturtle()
text.color("white")
style = ('Courier', 30, 'italic')
text.write(f"Score {score}", font = style)

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
    new_location = (randrange(200), randrange(200))
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
    return food

food = new_food()
    
# Check_collision

def check_collision(head, food):
    if head.distance(food.pos()) < 20:
        food.hideturtle()
        eat()
        return True
    

# Movement of snake
playing = True

def move(segments):
    for i in range(len(segments) - 1, 0, -1):
        segments[i].setpos(segments[i-1].pos())
    segments[0].forward(20)
        
def eat():
    position = segments[-1].pos()
    new = Turtle("square")
    new.up()
    new.color("white")
    new.goto(position)
    segments.append(new)

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

while playing:
    screen.update()
    move(segments)
    if check_collision(segments[0], food):
        food = new_food()
        score += 1
        text.clear()
        text.write(f"Score {score}", font=style)
    time.sleep(0.1)
    



screen.exitonclick()