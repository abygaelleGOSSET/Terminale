class Compte_bancaire:
    def __init__(self,solde,titulaire):
        self.solde=solde
        self.titulaire=titulaire
    def retirer_argent(self,montant):
        if self.solde<montant:
            print("T'es trop pauvre")
        else:
            self.solde=self.solde-montant
            print("Retrait effectué, vous avez", self.solde, "€")
    def deposer_argent(self,montant):
        self.solde=self.solde+montant
        print("Dépot effectué, vous avez", self.solde, "€")
        
        
        
lepetitbourge=Compte_bancaire(10, "Jean Louis Pasquier")


#Exercice 1
class Eleve:
    def __init__(self,nom,classe,note):
        self.nom=nom
        self.classe=classe
        self.note=note
    def a_la_moyenne(eleve):
        if eleve.note>=10:
            return True
        
def compare(eleve1,eleve2):
    if eleve1.note==eleve2.note:
        return (eleve1, eleve2)
    elif eleve1.note<eleve2.note:
        return eleve2.nom
    else:
        return eleve1.nom
    
        
Daisy=Eleve("Daisy","2nd",12)
Peach=Eleve("Peach","1ere",3)
Harmonie=Eleve("Harmonie","1ere",18)

#Exercice 2
class TriangleRectangle:
    def __init__(self,cote1,cote2,hypothenuse):
        self.cote1=cote1
        self.cote2=cote2
        self.hypothenuse=hypothenuse
        
def constructeur(cote1,cote2):
    
