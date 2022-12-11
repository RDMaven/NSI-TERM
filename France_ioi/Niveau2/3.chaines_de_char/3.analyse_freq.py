
def len_count(phrases:list, nbLignesMots:list):
    lens = {}
    for phrase in phrases:
        phrase:str
        mots = list(map(str, phrase.split()))
        for mot in mots : 
            if len(mot) in lens:
                lens[len(mot)] +=1
            else:
                lens[len(mot)] = 1
    print(*[(str(k) + " : " + str(v)) for k, v in sorted(lens.items(), key=lambda item: item[0])], sep='\n')


if __name__ == "__main__":
    nbLignesMots = list(map(int, input().split()))
    phrases = [str(input()) for _ in range(nbLignesMots[0])]
    len_count(phrases, nbLignesMots)

