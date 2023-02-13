from turtle import *

speed('slowest')

side = 10
size = 50

for i in range(side):
    forward(size)
    left(360/side)
    write(i)
    
hideturtle()
mainloop()
