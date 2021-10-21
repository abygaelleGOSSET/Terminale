from turtle import forward, up, down, left, right
from math import sqrt

#Exo 3
def carre(c):
    for i in range(4):
        forward(c)
        right(90)
    
def dessin(c,n):
    carre(c)
    forward(c/2)
    right(45)
    n=n-1
    while n>0:
        down
        a=c/2
        n=n-1
        c=sqrt(2*(a*a))
        carre(c)
        up
        forward(c/2)
        right(45)
   
##dessin(250,9)

#Exo 4
def trace(n,l):
    if n==1:
        forward(l)
    else:
        
        

