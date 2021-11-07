#Exercice 1
def moyenne(liste):
    haut=0
    bas=0
    for i in liste:
        haut=haut+i[0]*i[1]
        bas=bas+i[1]
    return haut/bas

# print(moyenne([(15,2),(9,1),(12,3)]))

#Exercice 2 
def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C
print(pascal(5))