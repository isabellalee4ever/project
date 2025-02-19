import turtle
class shapes:
    shape = turtle.Turtle()
    shape.speed(0)
    colors = ["#d45d55", "#77d47d", "#77d4bb", "#77c3d4", "#7798d4", "#8e77d4", "#d177d4", "#d4779b"]
    #8colors
    def triangle(len,x,y):
        shapes.shape.penup()
        shapes.shape.goto(x,y)
        shapes.shape.pendown()
        for i in range(3):
            shapes.shape.forward(len)
            shapes.shape.left(120)
    def square(len,x,y):
        shapes.shape.penup()
        shapes.shape.goto(x,y)
        shapes.shape.pendown()
        for i in range(4):
            shapes.shape.forward(len)
            shapes.shape.left(90)
    def spiral(r,x,y):
        shapes.shape.penup()
        shapes.shape.goto(x,y)
        shapes.shape.pendown()
        for i in range(r):
            for c in range(45):
                shapes.shape.forward(0.5 + (i/4))
                shapes.shape.left(5)
                shapes.shape.color(shapes.colors[c%8])
    def spiral2(r,x,y):
        shapes.shape.penup()
        shapes.shape.goto(x,y)
        shapes.shape.pendown()
        for c in range(r):
            shapes.shape.forward(c)
            shapes.shape.left(125)
            shapes.shape.color(shapes.colors[c%8])
s = shapes
s.spiral(70, 0, 0)
