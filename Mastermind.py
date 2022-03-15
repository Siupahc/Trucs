from pprint import pprint
import itertools
couleurs = ["blanc","rose","vert","rouge","orange","argent","jaune","bleu"]
combinaisons = list()
combinaisons = list(itertools.permutations(couleurs,4))
def bareme(x,y):
    blanc = 0
    rouge = 0
    i=0
    while i<=4 :
        if x[i]==y[i] :
            rouge+=1
        else :
            if x[i] in y :
                blanc+=1
        i+=1
    return (blanc,rouge)

def verification(x,y,z) :
    return bareme(x,y)==z
while len(combinaisons)>0 :
    a=input("Quelle est la première couleur? :")
    b=input("La deuxième ?:")
    c=input("La troisième? :")
    d=input("La dernière? :")
    blanc=int(input("Combien de blancs ?:"))
    rouge=int(input("Combien de rouges? :"))
    x=(a,b,c,d)
    z=(blanc,rouge)
    for y in combinaisons :
        if verification(x,y,z) == False :
            combinaisons.remove(y)
    print("Voici la liste des combinaisons possibles :")
    pprint(combinaisons)