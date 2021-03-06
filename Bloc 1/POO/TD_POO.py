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

#Exercice 2.1
from math import sqrt
class TriangleRectangle:
    def __init__(self,cote1,cote2,hypothenuse):
        self.cote1=cote1
        self.cote2=cote2
        self.hypothenuse=hypothenuse
    def constructeur(cote1,cote2):
        hypothenuse=sqrt(cote1**2+cote2**2)
        
triangle=TriangleRectangle(6,8,10)

#Exo 4
class Point:
    def __init__(self,coo):
        self.a=coo[0]
        self.b=coo[1]
        
    def __repr__(self):
        return "("+str(a)+","+str(b)+")"
    
    
#Exo 5
    
def pgcd(a,b):
    if b==0:
        return a
    else:
        return pgcd(b,b%a)
    
class Fraction:
    def __init__(self,num,denom):
        self.num=num/pgcd(num,denom)
        self.denom=denom/pgcd(num,denom)
    
    def __repr__(self):
       if self.denom==1:
           return str(self.num)
       else:
            return str(self.num)+"/"+str(self.denom)
    
    def __eq__(self,f2):
        return self.num/self.denom==f2.num/f2.denom
        
    def __lt__(self,f2):
        return self.num/self.denom<f2.num/f2.denom
    
    def __add__(self,f2):
        if self.denom==f2.denom:
            return Fraction(self.num+f2.num)
        else:
            return Fraction((self.num*f2.denom+f2.num*self.denom),(self.denom*f2.denom))
    
    def __mul__(self,f2):
        return Fraction((self.num*f2.num),(self.denom*f2.denom))
        
        
fraction=Fraction(10,2)
fraction2=Fraction(20,4)