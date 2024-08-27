import random
print("Quelle est le prix de l'objet X...?")
cible = random.randint(1,10)
print(cible)
for k in range (0,6) :
    if k > 4 :
        print("Vous avez perdu")
        break
    prop = int(input(f"Votre proposition entre 1 et 10 ({5-k} essais restants) :"))
    if prop > cible :
        print("Trop grand")
    elif prop < cible :
        print("Trop bas")
    else :
        print("Bravo!!!")
        break
