#Exercice 1
def RechercheMin(tab):
    m=tab[0]
    c=-1
    p=0
    for i in tab:
        c=c+1
        if i<m:
            m=i
            p=c
    return p
            
print(RechercheMin([5,3,2,2,4,1]))

#Exercice 2
def separe(tab):
    i = 0
    j = len(tab)-1
    while i < j :
        if tab[i] == 0 :
            i = i+1
        else :
            tab[i], tab[j] = tab[j],tab[i]
            j = j-1
    return tab

print(separe([1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,0]))