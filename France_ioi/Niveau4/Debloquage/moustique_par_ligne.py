def max_square(table, nbLignes, nbColonnes):
    
    for y in range(nbLignes):
        row = table[y]
        ranges = []
        one_range = []
        x = 0

        while x < nbColonnes:
            if row[x] == 0:
                one_range.append(x)
            else:
                if one_range != []:
                    ranges.append(one_range)
                    one_range = []
            x += 1
        if one_range != []:
            ranges.append(one_range)

        print(ranges)

if __name__ == "__main__":

    nbLignes, nbColonnes = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(nbLignes)]
    print(max_square(table, nbLignes, nbColonnes))