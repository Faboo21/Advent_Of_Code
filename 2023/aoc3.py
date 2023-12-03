import re

with open("2023/input.txt", 'r') as fichier:
    inputFinal = fichier.read()
with open("2023/inputTest.txt", 'r') as fichier2:
    inputTest = fichier2.read()

def v1(entree):
    
    entree = entree.split()
    for i in range(len(entree)) :
        tab = []
        ligne = entree[i]
        nb = [(int(s)) for s in re.findall(r"\d+", ligne)]
        for nombre in nb :
            tab.append([ligne.find(str(nombre)),nombre])
        for couple in tab:
            if (i > 0) :    
                if any("#+*$" in entree[i-1][couple[0]-1::couple[0]+len(str(couple[1]))]) :
                    print (entree[i-1][couple[0]-1:couple[0]+len(str(couple[1]))])
            
v1(inputTest)



