import pgzrun 

b = Rect((50,50), (100,50))
vx, vy = 3, 5                   #global variable

def draw():
    screen.fill('black')
    screen.draw.filled_rect(b, 'green')

def update():
    global vx, vy
    b.x += vx
    b.y += vx
    if b.right >800 or b.left < 0:
        vx = -vx
    if b.bottom > 600 or b.top < 0:
        vy = -vy

# outside of all function
pgzrun.go()