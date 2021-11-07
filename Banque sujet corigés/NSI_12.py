#Exercice 1
def maxi(tab):
    m=0
    c=-1
    p=0
    for i in tab:
        c=c+1
        if i>m:
            m=i
            p=c
    return m,p
     
#Exercice 2
def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = ...
    trouve = False
    while i < n and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            ...
        if j == g:
            trouve = True
        ...
    return trouve

print(recherche("AATC","GTACAAATCTTGCC"))