from turtle import *

speed('fastest')
pencolor('red')

for i in range(5):
    fd (100)
    for i in range(5):
        fd(50)
        for i in range(5):
            fd(50)
            rt(72)
        lt (72)
    rt(72)

hideturtle()
mainloop()


