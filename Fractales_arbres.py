from turtle import forward, backward, up, down, left, right


#Trace 2?
def trace(n,l):
    if n==0:
        forward(l)
    else:
        left(40)
        forward(l/1.5)
        backward(l/1.5)
        right(80)
        forward(l/1.5)
        backward(l/1.5)
        return trace(n-1,l/1.5)
                 
        
        
left(90)
trace(2,50)
        




##l=100
##left(90)
##forward(l)
##left(40)
##forward(l/1.5)
