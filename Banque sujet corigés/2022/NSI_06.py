#Exo 1
def maxi(tab):
    r=(0,0)
    for i in tab:
        if tab[i]>r[0]:
            r=(tab[i],i)
    return r

print(maxi([1,5,6,9,1,2,3,7,9,8]))

#Exo 2
def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j+=1
        if j == g:
            trouve = True
        i+=1
    return trouve


print(recherche("AATC","GTACAAATCTTGCC"))
