with open("2023/input.txt", 'r') as fichier:input = fichier.read()
with open("2023/inputTest.txt", 'r') as fichier:inputTest = fichier.read()

entree = inputTest

total = 0
input = entree.split()
truc = ["zero", "one","two","three","four","five","six","seven","eight","nine","0", "1","2","3","4","5","6","7","8","9"]
resultat = {"one" : 1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9, "zero": 0}

for ligne in input :
    tab = []
    for val in truc :
        a = ligne.find(str(val))
        if a != -1 :
            tab.append([a,val])
        a = ligne.rfind(str(val))
        if (a != -1) :
            tab.append([a,val])
    min = tab[0]
    max = tab[0]
    for val in tab :
        if (val[0] < min[0]) : min = val
        if (val[0] > max[0]) : max = val
        
    if (str(min[1]).isdigit()): 
        nb = str(min[1])
    else :
        nb = str(resultat[min[1]])
    if (str(max[1]).isdigit()): 
        nb += str(max[1])
    else :
        nb += str(resultat[max[1]])
    total += int(nb)
print (total + "cc")
