import random

def cree_arbre_complet(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre complet de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    l=[]
    if h==0:
        l.append(random.randint(0,maxi+1))
        l.append([])
        l.append([])
    else:
        cree_arbre_complet(h-1,maxi)

print(cree_arbre_complet(2,38))
