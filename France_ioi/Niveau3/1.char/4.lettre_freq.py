
def counter(phrase:str):
    recc = 0
   
    for i in set(phrase):
        c = phrase.count(i)
        if c > recc:
            recc = c
            max = i

    print(max)

if __name__ == "__main__":
    phrase = str(input()).upper().replace(" ", "")
    counter(phrase)