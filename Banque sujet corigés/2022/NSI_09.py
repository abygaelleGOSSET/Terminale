#Exo 1
def calcul(n):
    r=[n]
    while n!=1:
        if n%2==0:
            n=n//2
            r.append(n)
        else:
            n=n*3+1
            r.append(n)
    return r

#Exo 2
dico = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, \
        "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, \
        "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, \
        "T":20, "U":21,"V":22, "W":23, "X":24, "Y":25, "Z":26}

def est_parfait(mot) :
    #mot est une chaîne de caractères (en lettres majuscules)
    code_c = ""
    code_a = 0
    for c in mot :
        code_c = code_c + str(dico[c])
        code_a = code_a + dico[c]
    code_c = int(code_c)
    if code_a//code_c==0:
        mot_est_parfait = True
    else :
        mot_est_parfait = False
    return [code_a, code_c, mot_est_parfait]

print(est_parfait("PAUL"))