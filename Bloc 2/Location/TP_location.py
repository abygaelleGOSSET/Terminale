

2. Les clés primaires sont l'id pour la table Agences et Locations, et immatriculation pour la table Vehicules
3. Les 3 clés étrangères sont dans la table Locations, vehicule qui renvoie à immatriculation de Véhicules et depart et retour qui renvoie a l'id de Agences

# Relation Agences:

```sql
1. SELECT * FROM Agences
2. SELECT nom, ville FROM agences
3. SELECT nom FROM agences WHERE ville="Lorient"
4. SELECT nom, code FROM agences WHERE code like "56%"
5.
6. SELECT distinct ville FROM agences where code like "56%"
7.
8. SELECT count(nom) FROM agences where pays="France"
9.
```

# Relation Vehicules:

```sql
1. SELECT count(immatriculation) FROM vehicules
2. SELECT min(age) FROM Vehicules
   SELECT max(age) FROM Vehicules
3. SELECT nom FROM Vehicules where age=3
4. SELECT min(age) FROM Vehicules where nom like "Peugeot%"
5. SELECT max(kilometrage) FROM Vehicules
6. SELECT AVG(kilometrage) FROM Vehicules
7. SELECT kilometrage from Vehicules order by kilometrage desc
8. SELECT nom, immatriculation, (kilometrage/age) from Vehicules
9. SELECT immatriculation, max(kilometrage/age) from Vehicules where nom like "%Renault%"
10. SELECT nom ,immatriculation, round(kilometrage/age*0.35) as recette from Vehicules
11. SELECT nom, immatriculation from Vehicules order by (kilometrage/age*0.35) desc
```

# Relation Locations:
```sql
2. SELECT count(depart) FROM Locations
3. SELECT count(depart) FROM Locations WHERE depart!=retour
4.
5. SELECT AVG(kilometrage) FROM Locations WHERE depart=retour
6. SELECT * FROM locations JOIN Vehicules ON locations.vehicule=vehicules.immatriculation
7. SELECT Vehicules.nom, immatriculation, locations.date, locations.kilometrage FROM locations JOIN vehicules ON locations.vehicule=vehicules.immatriculation
8. 
```