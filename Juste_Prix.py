import random

def verif(prop,cible):
    if prop < 1 or prop > 10:
        print("Erreur ! Il faut choisir un prix entre 1 et 10")
        return "continuer"
    if prop > cible:
        print("Trop grand")
        return "continuer"
    elif prop < cible:
        print("Trop bas")
        return "continuer"
    else:
        print("Bravo!!!")
        return "bravo"

def juste_prix() :

    print("Quelle est le prix de l'objet X...?")
    cible = random.randint(1,10)
    #print(cible)
    for k in range (6) :
        if k > 4 :
            print("Vous avez perdu!!")
            break
        try :
            prop = int(input(f"Votre proposition entre 1 et 10 ({5-k} essais restants) :"))
        except ValueError:
            print("Erreur: Il faut choisir un entier")
            continue

        if verif(prop, cible) == "bravo":
            break
    print("Fin du jeu")
if __name__ == "__main__" :
    juste_prix()