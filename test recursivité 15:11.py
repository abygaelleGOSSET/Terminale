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