#Exo 1
def recherche(elt,tab):
    r=-1
    for i in range(len(tab)):
        if tab[i]==elt:
            r=i
            return r
    return r

print(recherche(15,[8,9,10,15,]))

#Exo 2
def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(tab)
    while a < i and i >= 0: 
      l[i+1] =  
      l[i] = a
      i = 
    return l