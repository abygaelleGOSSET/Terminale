def somme_recursif(n):
    if n == 0 :
        return 0
    else : 
        return n + somme_recursif(n-1)
    assert n>0, "impossible de calculer cette somme"
    
def somme_iteratif(n):
    total=0
    for i in range(1,n+1):
        total=total+i
    return total
    assert n>0, "impossible de calculer cette somme"


print(somme_iteratif(-4))

#Q2. Le récursif
#b. Elle est plus instinctive
#Q3. Il donne le temps que met le code récursif à calculer 1+2+..+1000

import timeit

timeit.timeit('somme_iteratif(1000)', number=50, setup="from __main__ import somme_iteratif")

#Q4. Elle met moins de temps
#Q5. Une erreur, parce que comme c'est négatif, il n'atteindra jamais 0 vu qu'on enlève, il faudrait ajouter.
#b. Un range ne peut pas aller à l'envers?