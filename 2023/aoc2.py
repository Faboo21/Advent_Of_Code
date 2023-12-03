def v1(input):
    input = input.split("\n")

    max_rouge,max_bleu,max_vert = 12,14,13

    total = 0

    for ligne in input :
        ligne = ligne.split(":")
        games = ligne[1].split(";")
        bool = True
        for game in games :
            tir = game.split(',')
            for lance in tir :
                numbers = [int(temp) for temp in lance.split() if temp.isdigit()]
                if "blue" in lance :
                    if max_bleu < int (numbers[0]) : bool = False
                if "red" in lance :
                    if max_rouge < int (numbers[0]) : bool = False
                if "green" in lance :
                    if max_vert < int (numbers[0]) : bool = False
        if bool != False :
            total+= [int(temp) for temp in ligne[0].split() if temp.isdigit()][0]
    print (total)
def v2(input):
    input = input.split("\n")

    total = 0

    for ligne in input :
        ligne = ligne.split(":")
        games = ligne[1].split(";")
        max_bleu = 0
        max_rouge = 0
        max_vert = 0
        for game in games :
            tir = game.split(',')
            for lance in tir :
                val = int([int(temp) for temp in lance.split() if temp.isdigit()][0])
                if "blue" in lance :
                    if val > max_bleu : max_bleu = val
                if "red" in lance :
                    if val > max_rouge : max_rouge = val
                if "green" in lance :
                    if val > max_vert : max_vert = val
        total += max_rouge*max_vert*max_bleu
    print (total)


v2(input)