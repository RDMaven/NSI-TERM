
def multiple(nbPersonnes, nbFruits):
    if nbFruits%nbPersonnes == 0:
        print("oui")
    else:
        print("non")

if __name__ == "__main__":
    nbPersonnes = int(input())
    nbFruits = int(input())

    multiple(nbPersonnes, nbFruits)