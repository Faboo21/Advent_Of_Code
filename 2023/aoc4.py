with open("2023/input.txt", 'r') as fichier:input = fichier.read()
with open("2023/inputTest.txt", 'r') as fichier:inputTest = fichier.read()

def v1(entree):
    total = 0

    input = entree.split("\n")
    for ligne in input:
        cpt = 0
        bon = [val for val in ligne.split(":")[1].split("|")[0].split(" ") if val != '']
        res = [val for val in ligne.split(":")[1].split("|")[1].split(" ") if val != '']
        for nb in res:
            if nb in bon :
                if cpt == 0 :
                    cpt = 1
                else :
                    cpt *= 2
        total += cpt
    print (total)

def v2(entree):
    cartes = entree.split("\n")
    cartesBase = entree.split("\n")
    for carte in cartes:
        cpt = 0
        bon = [val for val in carte.split(":")[1].split("|")[0].split(" ") if val != '']
        res = [val for val in carte.split(":")[1].split("|")[1].split(" ") if val != '']
        for nb in res:
            if (nb in bon):
                cpt+= 1
                nbcarte = cartesBase.index(carte)
                cartes.append(cartesBase[nbcarte + cpt])
    print(len(cartes))
    
v2(inputTest)