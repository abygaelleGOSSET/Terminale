#Exercice 1
def moyenne(tab):
    assert tab!=[], "erreur"
    m=0
    for i in tab:
        m=m+i
    return m/len(tab)

print(moyenne([5,3,8]))

#Exercice 2
def tri(tab):
        #i est le premier indice de la zone non triée, j le dernier indice
        #Au debut, la zone non triée est le tableau entier.
        i=0
        j=len(tab)-1
        while i!=j:
            if tab[i]==0:
                i+=1
            else:
                valeur=tab[j]
                tab[j]=tab[i]
                tab[i]=valeur
                j-=1
        return tab
    
print(tri([0,1,0,1,0,1,0,1,0,1]))
