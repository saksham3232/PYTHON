import turtle

wn = turtle.Screen()

elan = turtle.Turtle()
wn.screensize(2000, 1500)
distance = 50
elan.speed(6)
for _ in range(10):
    elan.forward(distance)
    elan.right(90)
    distance += 10
    

wn.exitonclick()