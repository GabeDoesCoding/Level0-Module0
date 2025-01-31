import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    joe = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    joe.shape('turtle')
    # Set your turtle's speed using .speed(2)
    joe.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    joe.color('green')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
   # for i in range(4) :
     #   joe.left(90)
      #  joe.forward(100)

    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    joe.goto(0, 0)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    #joe.begin_fill()
  #  joe.circle(180, steps=60)
   # joe.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    joe.begin_fill()
    joe.left(120)
    joe.forward(100)
    joe.left(120)
    joe.forward(100)
    joe.left(120)
    joe.forward(100)
    joe.end_fill()
    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
