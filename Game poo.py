import random
import sys

class Personnage:
    def __init__(self, nom, points_de_vie, competences):
        self.prenom=nom
        self.vie = points_de_vie
        self.aptitudes_combat=competences
 
    def perd_vie(self):
        if random.random()*10>self.aptitudes_combat:
            nbPoint=1
        else:
            nbPoint=0
        self.vie = self.vie - nbPoint
        return nbPoint
    
def game(p1,p2):
    while p1.vie> 0 and p2.vie > 0:
        perte1=p1.perd_vie()
        print("\033[34m")
        print(p1.prenom+" perd "+ str(perte1)+ " point de vie, il lui en reste "+str(p1.vie))
        print("\033[32m")
        perte2=p2.perd_vie()
        print(p2.prenom+" perd "+str(perte2)+" point de vie, il lui en reste "+str(p2.vie)) 

    print("\033[30m")
    if p1.vie<= 0 and p2.vie> 0:
        msg = p2.prenom+" est vainqueur, il lui reste encore " + str(p2.vie) + " points alors que "+p1.prenom+" est mort"
    elif p2.vie <= 0 and p1.vie > 0:
        msg = p1.prenom+" est vainqueur, il lui reste encore " + str(p1.vie) + " points alors que "+p2.prenom+" est mort"
    else:
        msg = "Les deux combattants sont morts en même temps"

    return msg

bilbo = Personnage("Bilbo",5,4)
gollum = Personnage("Gollum",5,2)
frodon = Personnage("Frodon", 5,3)
araignee = Personnage("Araignée", 5,3)
aragorn = Personnage("Aragorn", 5, 2)

print(game(bilbo,gollum))
