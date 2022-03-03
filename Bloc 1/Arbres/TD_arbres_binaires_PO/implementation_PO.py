from visualisation_arbre import *
from random import randint

# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 2
arbre_cours=[2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]]
show(arbre_cours,"arbre_du_cours")

# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 3
arbre_vide=[]
arbre_feuille=[1,[],[]]
show(arbre_feuille,"feuille")

# # PARTIE 2 - CODE ET TESTS A ECRIRE


def est_vide(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Détermine si un arbre est vide
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si l'arbre est vide, False sinon
    
    TESTS :
    >>> est_vide(arbre_vide)
    True
    
    >>> est_vide(arbre_feuille)
    False
    
    >>> est_vide(arbre_cours)
    False
    '''
    return arbre==[]

def est_feuille(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Détermine si l'arbre est une feuille
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si l'arbre est une feuille, False sinon
    
    TESTS :
    >>> est_feuille(arbre_vide)
    False
    
    >>> est_feuille(arbre_feuille)
    True
    
    >>> est_feuille(arbre_cours)
    False
    '''
    if est_vide(arbre)==True:
        return False
    return arbre[1]==[] and arbre[2]==[]


def racine(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie la valeur du noeud racine
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int, str, etc...) : Valeur du noeud racine
    précondition : L'arbre ne doit pas être vide
    
    TESTS :
    >>> racine(arbre_feuille)
    1
    
    >>> racine(arbre_cours)
    2
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
    assert est_vide(arbre)==False, "L'arbre est vide"
    return arbre[0]

def SAG(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie le sous-arbre gauche de l'arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (list) : sous-arbre gauche
    précondition : L'arbre ne doit pas être vide
    
    TESTS :
    >>> SAG(arbre_feuille)
    []
    
    >>> SAG(arbre_cours)
    [8, [6, [], []], [9, [], []]]
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
    assert est_vide(arbre)==False, "L'arbre est vide et n'a donc pas d'abre gauche" # A compléter
    return arbre[1]

def SAD(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie le sous-arbre droit de l'arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (list) : sous-arbre droit
    précondition : L'arbre ne doit pas être vide
    
    TESTS :
    >>> SAD(arbre_feuille)
    []
    
    >>> SAD(arbre_cours)
    [1, [7, [], []], []]
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail) 
    assert est_vide(arbre)==False, "L'arbre est vide et n'a donc pas d'arbre droit"
    return arbre[2]

def taille(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Calcule la taille d'un arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int) : Taille de l'arbre
    
    TESTS :
    >>> taille(arbre_vide)
    0
    
    >>> taille(arbre_feuille)
    1
    
    >>> taille(arbre_cours)
    6
    '''
    if est_vide(arbre) :
        return 0
    else:    
        return 1+taille(SAG(arbre))+taille(SAD(arbre))

        
def hauteur(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Calcule la hauteur d'un arbre en respectant la convention
            donnée dans l'énoncé
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int) : Hauteur de l'arbre
    
    TESTS :
    >>> hauteur(arbre_vide)
    -1
    
    >>> hauteur(arbre_feuille)
    0
    '''
    if est_vide(arbre):
        return -1
    elif est_feuille(arbre):
        return 0
    else:
        return 1+max(hauteur(SAG),hauteur(SAD))

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
    for i in range(h):
        c=0
        while c!=2:
            l.append(randint(0,maxi+1))
            c+1

def cree_peigne_gauche(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne gauche de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    # A compléter

def cree_peigne_droit(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne droit de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    # A compléter

def est_egal(arbre1, arbre2):
    '''
    DOCUMENTATION :
    Description de la fontion : détermine si deux arbres sont identiques ou différents
    arbre1 (list) : Arbre implémenté sous forme de listes imbriquées
    arbre2 (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si les deux arbres sont identiques, False sinon 
    
    TESTS :
    >>> est_egal([2,[3,[],[]],[]],[2,[3,[],[]],[]])
    True
    
    >>> est_egal([2,[3,[],[]],[]],[7,[6,[],[]],[]])
    False
    
    >>> est_egal([2,[3,[],[]],[]],[])
    False
    '''
    return arbre1==arbre2

if __name__ == '__main__':
    # Lancement des tests (laisser ces deux lignes de code inchangées)
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    
    arbre_complet=cree_arbre_complet(3,9)
    peigne_gauche=cree_peigne_gauche(3,9)
    peigne_droit=cree_peigne_droit(3,9)
    
print(arbre_complet)
print(peigne_gauche)
print(peigne_droit)
show(arbre_complet,"complet")
show(arbre_gauche,"peigne gauche")
show(arbre_droit,"peigne droit")

    
    # PARTIE 2 - Question 4 
    # A compléter
