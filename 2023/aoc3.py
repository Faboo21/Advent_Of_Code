from copy import copy

with open("2023/input.txt", 'r') as fichier:input = fichier.read()
with open("2023/inputTest.txt", 'r') as fichier:inputTest = fichier.read()

def affichetab(tab):
    for ligne in tab: print (ligne)

def v1(entree):
    input = entree.split("\n")
    for i in range(len(input)):
        input[i] = '.' + input[i] + '.'
        for char in  ['+', '-', '*', '/', '(', ')', '@','%','&','=','$','#']:
            input[i] = input[i].replace(char,'#')
    input.insert(0,'.'*(len(input[0])))
    input.append('.'*(len(input[0])))
    
    total = 0
    for i in range(1,len(input)-1):
        numbers = input[i].replace('.',' ').replace("#"," ")
        numbers = [int(temp) for temp in numbers.split() if temp.isdigit()]
        temp = copy(input[i])
        for nombre in numbers:
            taille = len(str(nombre))
            pos = temp.find(str(nombre))
            temp = temp.replace(str(nombre),"."*taille)
            print(input[i - 1][pos-1:pos+taille+1])
            print(input[i][pos-1:pos+taille+1])
            print(input[i + 1][pos-1:pos+taille+1])
            print()
            #surement un pb de plusieurs occurence dans une liste
            if ("#" in input[i - 1][pos-1:pos+taille+1]) or ("#" in input[i][pos-1:pos+taille+1]) or ("#" in input[i + 1][pos-1:pos+taille+1]):
                total += nombre
    print (total)
    
v1(input)