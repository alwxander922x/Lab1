import turtle
aze = turtle.Turtle()

aze.shape('turtle')
aze.speed(400)
def makeStar():
        for k in range(5):
            aze.forward(20)
            aze.right(144)

for i in range(12):
        makeStar()
        aze.left(30)
        aze.penup()
        aze.forward(50) 
        aze.pendown()
turtle.mainloop()
