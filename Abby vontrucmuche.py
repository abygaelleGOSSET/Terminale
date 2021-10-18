import turtle

def von_koch(o,l):
    if o==0:
        turtle.forward(l)
    else:
        turtle.forward(l)
        turtle.left(60)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
        turtle.left(60)
        turtle.forward(l)
        turtle.left(60)
        von_koch(o-1,l/4)
        
print(von_koch(3,100))