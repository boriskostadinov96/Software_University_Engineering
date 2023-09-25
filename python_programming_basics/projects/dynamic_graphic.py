import turtle as tt
tt.Screen().bgcolor('black')
tt.pensize(2)
tt.speed(20)

for i in range (6):
    for color in ('red', 'magenta', 'blue', 'cyan', 'green', 'white', 'yellow'):

        tt.color(color)
        tt.circle(100)
        tt.left(10)

        tt.hideturtle()

tt.done()