def puissance(a,n):
    if n==1:
        return a
    else:
        return a*puissance(a,n-1)
    
print(puissance(2,5))

def somme_iteratif(n):
    pas=0
    total=0
    while pas-1<n:
        total=total+pas
        pas=pas+1
    return total


def somme_recursif(n):
    if n == 0 :
        return 0
    else : 
        return n + somme_recursif(n-1)
    
print(somme_iteratif(-4))

#Exercice 7
def nombre_de_chiffres(x):
    """
    description: Donne le nombre de chiffres contenu dans un nombre x
    paramètre(int)
    return(int)
    """
    assert x>0, "Cette fonction ne fonctionne que pour des entiers naturels"
    if x<10:
        return 1
    else:
        return (nombre_de_chiffres(x//10) +1) 
    

#Exercice 8

def appartient(m,l,i):
    if m==l[i]:
        return True
    elif i==len(l)-1:
        return False
    else:
        return appartient(m,l,i+1)
        
##print(appartient('spam', ['foo', 'bar', 'spam', 'ham', 'eggs'], 3))


#Exercice 9

def est_palindrome(c):
    for i in range(len(c)):
        if c[i]==c[i-1]:
            return True  #Il renvoie true pour la première lettre seulement, il ne fait pas de tour de boucle
        else:
            return False
        
print(est_palindrome("pabp"))
##def palindromer(c,p):
##    if :
##    else:
##        return palindromer()