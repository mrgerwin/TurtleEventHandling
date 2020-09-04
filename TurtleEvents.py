import turtle

#When you test it, make sure you click on the screen first before you perform events

def up():
  tina.forward(50)
  
def down():
  tina.backward(50)
  tina.setheading(int(tina.heading())-180)
  
def left():
  tina.left(90)
  tina.forward(50)

def right():
  tina.right(90)
  tina.forward(50)
  
def get_coords(x, y):
  print(x,y)
  tina.setheading(tina.towards(x,y))
  tina.goto(x,y)

tina = turtle.Turtle()
tina.write("Use the arrows or click")
myscreen = turtle.Screen()
myscreen.onclick(get_coords)
myscreen.onkey(up, "Up")
myscreen.onkey(down, "Down")
myscreen.onkey(left, "Left")
myscreen.onkey(right, "Right")

myscreen.listen()
