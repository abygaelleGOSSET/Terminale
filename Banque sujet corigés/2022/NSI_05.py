#Exo 1
def rechercheMinMax(tab):
    r={'min':tab[0],'max':tab[0]}
    if tab==[]:
        r={'min':None,'max':None}
        return r
    for e in tab:
        if e>r['max']:
            r['max']=e
        elif e<r['min']:
            r['min']=e
    return r

#Exo 2
class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
        for i in range(52):
            for c in range(4):
                for n in range(13):
                    self.contenu.append(Carte(c,n))
