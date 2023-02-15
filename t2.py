from turtle import *

pencolor('green')
pensize(3)
fillcolor('red')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()
       
mainloop()

wap to print if the length of a string is even or, from a list of string