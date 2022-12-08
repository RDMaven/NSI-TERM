
def sortir(nb_deplacements, deplacements):
    dep = {1:2, 2:1, 3:3, 4:5, 5:4}
    print(*[dep[i] for i in deplacements[::-1]], sep="\n")

if __name__ == "__main__":
    nb_deplacements = int(input())
    deplacements = [int(input()) for _ in range(nb_deplacements)]
    
    sortir(nb_deplacements, deplacements)

