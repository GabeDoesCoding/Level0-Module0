import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    joe = turtle.Turtle()
    # This code sets our shape to a turtle
    joe.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    joe.speed=10
    # Set your turtle's color using .color('green')
    joe.color('green')
    # Use a loop to repeat a the code below 50 times
    for i in range(50) :
         joe.color(get_random_color())
         joe.forward(5*i)
         joe.right(360/7)
         joe.width(i)
        # Set the turtle color to a random color

        # Move the turtle (5*i) pixels. 'i' is the loop variable
        
        # Turn the turtle (360/7) degrees to the right
         
        # Change the turtle width to 'i' (the loop variable)
        
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
