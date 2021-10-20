import turtle

def von_koch(n,l):
    if n==0:
        turtle.forward(l)
    else:
        von_koch(n-1,l/3)
        turtle.left(60)
        von_koch(n-1,l/3)
        turtle.right(120)
        von_koch(n-1,l/3)
        turtle.left(60)
        von_koch(n-1,l/3)

        
print(von_koch(4,500))