import turtle
t= turtle.Turtle()
t.speed(10)
colors= ["red","orange","yellow","green","blue","purple"]
for i in range(36):
    t.color(colors[i%6])
    t.forward(200)
    t.right(170)
turtle.done()