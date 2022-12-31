

if __name__ == "__main__":
    somme = 0
    try:
        while True : 
            somme += sum(list(map(int, input().split())))
    except:
        print(somme)
