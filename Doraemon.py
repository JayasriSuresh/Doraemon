import turtle

 
# Creating a turtle object(pen)
pen = turtle.Turtle()
pen.hideturtle()

# Defining method to draw a colored circle
# with a dynamic radius
def ring(col, rad):
 
    # Set the fill
    pen.fillcolor(col)
 
    # Start filling the color
    pen.begin_fill()
 
    # Draw a circle
    pen.circle(rad)
 
    # Ending the filling of the color
    pen.end_fill()



# Blue face 
pen.up()
pen.setpos(0, -150)
pen.down()
ring('#00a0de', 150)

# White face
pen.up()
pen.setpos(-120, 10)
pen.down()
pen.right(120)
for i in range(2):
  pen.fillcolor('white')
  pen.begin_fill()
  pen.circle(150//2,60)
  pen.circle(137,120)
  pen.end_fill()

# Right eye Background
pen.up()
pen.setpos(27, 114)
pen.down
pen.right(88)
for j in range(2):
  pen.fillcolor("black")
  pen.begin_fill() 
  pen.circle(25//2,60)
  pen.circle(35,120)
  pen.end_fill()

# Left eye Background
pen.up()
pen.setpos(-15, 114)
pen.down
pen.right(7)
for l in range(2):
  pen.fillcolor("black")
  pen.begin_fill() 
  pen.circle(25//2,60)
  pen.circle(35,120)
  pen.end_fill()

# Left eye White
pen.up()
pen.setpos(-15, 109)
pen.down
pen.right(2)
for m in range(2):
  pen.fillcolor("white")
  pen.begin_fill() 
  pen.circle(21//2,60)
  pen.circle(31,120)
  pen.end_fill()

# Right eye White
pen.up()
pen.setpos(29, 110)
pen.down
pen.right(-4)
for k in range(2):
  pen.fillcolor("white")
  pen.begin_fill() 
  pen.circle(21//2,60)
  pen.circle(31,120)
  pen.end_fill()

# Right eye ball
pen.up()
pen.setpos(21, 93)
pen.down
pen.right(-4)
for k in range(2):
  pen.fillcolor("black")
  pen.begin_fill() 
  pen.circle(10//2,60)
  pen.circle(15,120)
  pen.end_fill()

# Left eye ball
pen.up()
pen.setpos(-18, 93)
pen.down
pen.right(0)
for k in range(2):
  pen.fillcolor("black")
  pen.begin_fill() 
  pen.circle(10//2,60)
  pen.circle(15,120)
  pen.end_fill()

# Left eye Pupil
pen.up()
pen.setpos(-18, 86)
pen.down
pen.right(0)
for k in range(2):
  pen.fillcolor("white")
  pen.begin_fill() 
  pen.circle(5//2,60)
  pen.circle(7,120)
  pen.end_fill()

# Right eye Pupil
pen.up()
pen.setpos(20, 86)
pen.down
pen.right(0)
for k in range(2):
  pen.fillcolor("white")
  pen.begin_fill() 
  pen.circle(5//2,60)
  pen.circle(7,120)
  pen.end_fill()

# Nose
pen.up()
pen.setpos(6, 63)
pen.down()
ring('Red', 15)

# Line Bellow the Nose
pen.up()
pen.setpos(-1, -93)
pen.down()
pen.seth(90)
pen.forward(130)

# Smile
pen.up()
pen.setpos(95, 6)
pen.down()
pen.circle(100,-180)

# Cat Whisks
pen.up()
pen.setpos(-30, 5)
pen.down()
pen.seth(155)
pen.forward(80)

pen.up()
pen.setpos(-30, -10)
pen.down()
pen.seth(180)
pen.forward(80)

pen.up()
pen.setpos(-30, -25)
pen.down()
pen.seth(205)
pen.forward(80)

pen.up()
pen.setpos(30, 5)
pen.down()
pen.seth(25)
pen.forward(80)

pen.up()
pen.setpos(30, -10)
pen.down()
pen.seth(0)
pen.forward(80)

pen.up()
pen.setpos(30, -25)
pen.down()
pen.seth(335)
pen.forward(80)

# My Name
pen.up()
pen.setpos(110, -175)
pen.down()
pen.write('By Jayasri Suresh', font=("Comic Sans MS", 10, "bold"))
