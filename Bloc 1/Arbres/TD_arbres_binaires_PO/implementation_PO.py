from visualisation_arbre_PO import *
from random import randint

# IMPLEMENTATION DE LA CLASSE NOEUD

class Noeud:
    def __init__(self, valeur, gauche, droit):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

# PARTIE 2 - CODE ET TESTS A ECRIRE

class Arbre:
    def __init__(self, noeud=None):
        self.racine = noeud

    def est_vide(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Détermine si l'arbre est vide
        return (bool) : True si l'arbre est vide, False sinon
        
        TESTS :
        >>> arbre_cours.est_vide()
        False
        
        >>> arbre_vide.est_vide()
        True
        
        >>> arbre_feuille.est_vide()
        False
        '''
        return self.racine==None

    def est_feuille(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Détermine si l'arbre est une feuille
        return (bool) : True si l'arbre est une feuille, False sinon
        
        TESTS :
        >>> arbre_cours.est_feuille()
        False
        
        >>> arbre_vide.est_feuille()
        False
        
        >>> arbre_feuille.est_feuille()
        True
        '''
        if self.est_vide():
            return False
        return self.racine.gauche is None and self.racine.droit is None
    
    def valeur_racine(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie la valeur de la racine de l'arbre
        return (int, str, etc...) : Valeur de la racine de l'arbre
        précondition : Il faut que l'arbre ait une racine
        
        TESTS :
        >>> arbre_cours.valeur_racine()
        2
        
        >>> arbre_feuille.valeur_racine()
        3
        '''
        # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
        assert not self.est_vide(), "L'arbre n'a pas de racine." # A compléter
        return self.racine.valeur

    def SAG(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie le sous-arbre gauche de l'arbre
        return (Arbre) : sous-arbre gauche
        précondition : Il faut que l'arbre ait un sous arbre gauche (qu'il ne soit ni vide, ni feuille)
        
        TESTS :
        >>> affiche(arbre_cours.SAG())
        (8, 6, 9)
        
        >>> arbre_feuille.SAG()
        
        '''
        # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
        assert not self.est_vide(), "L'arbre n'a pas de sous arbre gauche"
        return Arbre(self.racine.gauche)
    
    def SAD(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie le sous-arbre droit de l'arbre
        return (Arbre) : sous-arbre droit
        précondition : Il faut que l'arbre ait un sous arbre droit (qu'il ne soit ni vide, ni feuille)
        
        TESTS :
        >>> arbre_cours.SAD()
        Noeud(1, Noeud(7, None, None), None)
        
        
        >>> arbre_feuille.SAD()
        
        '''
        
        assert not self.est_vide() , "L'arbre n'a pas de sous arbre droit"
        return self.racine.droit
    
    def taille(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Calcule la taille d'un arbre
        return (int) : Taille de l'arbre
        
        TESTS :
        >>> arbre_vide.taille()
        0
        
        >>> arbre_feuille.taille()
        1
        
        >>> arbre_cours.taille()
        6
        '''
        if self.est_vide():
            return 0
        return 1+self.racine.SAG.taille()+self.racine.SAD.taille()

    def hauteur(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Calcule la hauteur d'un arbre en respectant la convention
                donnée dans l'énoncé
        return (int) : Hauteur de l'arbre
        
        TESTS :
        '''
        #A compléter

    def est_egal(self, arbre):
        '''
        DOCUMENTATION :
        Description de la fontion : détermine si deux arbres sont identiques ou différents
        arbre (Arbre) : arbre sur lequel on va tester l'égalité
        return (bool) : True si les deux arbres sont identiques, False sinon 
        
        TESTS :
        '''
        #A compléter   

def cree_arbre_complet(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre complet de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter   
        
def cree_peigne_gauche(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne gauche de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter 

def cree_peigne_droit(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne droit de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter
    

if __name__ == '__main__':
    # Lancement des tests (laisser ces deux lignes de code inchangées)
    import doctest
        
    noeud = Noeud(2, Noeud(8, Noeud(6, None, None), Noeud(9, None, None)), Noeud(1, Noeud(7, None, None), None))
    arbre_cours = Arbre(noeud)
    #show(arbre_cours,"arbre_du_cours")

    arbre_vide=Arbre()

    noeud2=Noeud(3,None,None)
    arbre_feuille=Arbre(noeud2)
    #show(arbre_feuille,"feuille")
        
    # Creation d'un arbre complet de hauteur 3
        # A compléter
    
    # Creation d'un peigne gauche de hauteur 3
        # A compléter
    
    # Creation d'un peigne droit de hauteur 3
        # A compléter

# PARTIE 2 - Question 4
    # A compléter
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)