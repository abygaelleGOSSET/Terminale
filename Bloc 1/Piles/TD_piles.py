class Pile:
    def creer_pile():
    """ Créé une pile vide
    :return: Une pile vide représentée par la liste vide
    """
    return []


    def est_vide(p):
    """ Teste si une pile est vide
    :param p: Une pile
    :return: True si p est vide, False sinon
    """
        return p == []


    def empiler(p, e):
    """ Empile un élément au sommet d'une pile
    :param p: Une pile
    :param e: Un élément
    :return: None
    :Effets: Empile e au sommet de p
    """
        p.append(e)
    

    def depiler(p):
    """ Dépile un élément au sommet d'une pile et le renvoie
    :param p: Une pile
    :return: L'élément au sommet de la pile
    :Précondition: p est non vide
    """
        assert not est_vide(p), "Impossible de dépiler une pile vide"
        return p.pop()

    def pile_alternee(pile,n):
        for i in range(0,n+1):
            if i%2!=0:
                empiler(pile,-i)
            else:
                empiler(pile,i)
        return pile

            
#Exo 2
    def vider_pile(pile):
        while not est_vide(pile):
            depiler(pile)
        
    def sommet_pile(pile):
        n=depiler(pile)
        empiler(pile,n)
        return n

#Exo 3
    def est_bien_parenthesee(str):
        pile=creer_pile()
        for i in str:
            if i=="(":
                empiler(pile,"(")
            else:
                if est_vide(pile):
                    return False
                else:
                    depiler(pile)
        return True
        


#Exo 4
    def separer_expression(exp):
        return exp.split(" ")

    def evaluer_postfixee(post):
        nouvelle=separer_expression(post)
        pilenombre=creer_pile()
        for e in post:
            if not est_operateur(e):
                empiler(pilenombre,e)
            else:
            
#Exo 7
    #Partie 1
            
    def est_balise_fermante(a):
        return a[0]=="<" and a[1]=="/" and a[len(a-1)]==">"

    
    def est_paire_balise(a,b):
        if a!=est_balise_fermante(a):
            return False
        for i in a:
            if a[i]=="<" or ">" or "/":
                None
            else:
                if a[i]!=b[i]:
                    return False
        return True
    #Partie 2
    def verifier_html(s1):
        s=html_to_str(s1)
        p=creer_pile()
        parser=MyHTMLParser(s)
        for e in parser:
            if e=="<"
