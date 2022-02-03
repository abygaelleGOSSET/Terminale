class File:
    def __init__(self): # Les éléments sont stockés dans une liste python
        self.data = []
      
    def est_vide(self):
        return len(self.data) == 0 
    
    # Le choix suivant a été fait : La tête de la file correspond au premier élément de la liste 
    #                               (et la queue au premier élément de la liste)
    
    def enfile(self,x):
        self.data.append(x)

    def defile(self):
        assert not self.est_vide(), "Vous avez essayé de défiler une file vide !"
        return self.data.pop(0)
    
    def defile_v2(self):
        assert not self.est_vide(), "Vous avez essayé de défiler une file vide !"
        return self.data[1:self.taille()]
    
    def taille(self):
        return len(self.data)
    

    def __repr__(self):       # pour afficher convenablement la file             
        """
        Affiche le contenu d'une file
        La tête de file est affichée à gauche et la queue à droite
        """
        s = "|"
        for i in range(len(self.data)) :
            s = s + str(self.data[i]) + "|"
        return s
    

class File2:
    def __init__(self): # Les éléments sont stockés dans une liste python
        self.data = []
      
    def est_vide(self):
        return len(self.data) == 0 
    
    # Le choix suivant a été fait : La tête de la file correspond au premier élément de la liste 
    #                               (et la queue au premier élément de la liste)
    
    def enfile(self,x):
        self.data.append(x)

    def defile(self):
        assert not self.est_vide(), "Vous avez essayé de défiler une file vide !"
        return self.data.pop(self.taille)
    
    def taille(self):
        return len(self.data)
    

    def __repr__(self):       # pour afficher convenablement la file             
        """
        Affiche le contenu d'une file
        La tête de file est affichée à gauche et la queue à droite
        """
        s = "|"
        for i in range(len(self.data)) :
            s = s + str(self.data[i]) + "|"
        return s


#Exo 6
from pile import *
class File2:
    def __init__(self):
        self.pe=Pile()
        self.ps=Pile()
    
    def enfile(self,x):
        self.pe.empiler(x)
        
    def defile(self):
        if self.ps.est_vide:
            if self.pe.est_vide:
                return "File vide"
            self.ps.empiler(pe.depile())
        return self.ps.depiler()
            
        
    def est_vide(self):
        return len(pe) and len(ps)==0
    
file=File2()
file.enfile(4)
file.enfile(6)
file.enfile(6)
file.defile()