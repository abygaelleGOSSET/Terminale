##    #Partie 2
##def verifier_html(s1):
##    s=html_to_str(s1)
##    p=creer_pile()
##    parser=MyHTMLParser(s)
##    while parser.has_tag():
##        balise = parser.next_tag()
##        if est_balise_fermante(balise)==False:
##            empiler(p, balise)
##        if est_balise_fermante(balise)==True and est_vide(p)==False:
##            
##            
##        else:
##            return False
            
from myhtml_parser import html_to_str, MyHTMLParser

balise = parser.next_tag()