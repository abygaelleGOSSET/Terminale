#Exo 1
def recherche(tab):
    r=[]
    for i in range(1,len(tab)):
        if tab[i]==tab[i-1]+1:
            r.append((tab[i-1],tab[i]))
    return r

#Exo 2

def propager(M,i,j,val):
    if M[i][j]==0:
        return M
    M[i][j]=val
    
    #L'élément en haut fait partie de la composante
    if((i-1)>=0 and M[i-1][j]==1):
        propager(M,i-1,j,val)
        
    #L'élément en bas fait partie de la composante
    if((i+1)<len(M) and M[i+1][j]==1):
        propager(M,i+1,j,val)
        
    #L'élément à gauche fait partie de la composante
    if((j-1)>=0 and M[i][j-1]==1):
        propager(M,i,j-1,val)
    
    #L'élément à droite fait partie de la composante
    if((j+1)<len(M) and M[i][j+1]==1):
        propager(M,i,j+1,val)
        
M=[[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]
propager(M,2,1,3)
print(M)
        
        
    
