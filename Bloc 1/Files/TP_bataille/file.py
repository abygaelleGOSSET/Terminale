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
