class Pile:
    def creer_pile():
        return []


    def est_vide(p):
        return p == []


    def empiler(p, e):
        p.append(e)


    def depiler(p):
        assert not est_vide(p), "Impossible de dépiler une pile vide"
        return p.pop()


    def afficher_pile(p):
        print("-" * 20)
        for element in p[::-1]:
            print("|" + " " * 18 + "|")
            print("|" + str(element).center(18) + "|")
            print("|" + " " * 18 + "|")
            print("-" * 20)
        print("-" * 20)