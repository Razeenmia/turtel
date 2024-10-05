import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed (1 is slowest, 10 is fastest)
t.speed(5)

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Keep the window open until it's clicked
turtle.done()
for _ in range(6):
    t.forward(100)
    t.right(60)