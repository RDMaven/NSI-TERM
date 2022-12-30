"""
Votre programme doit d'abord lire un entier, la population totale de la ville. Sachant qu'une personne était malade au jour 1 et que chaque malade contamine deux nouvelles personnes le jour suivant (et chacun des jours qui suivent), vous devez calculer à partir de quel jour toute la population de la ville sera malade.

"""

def contamination(population):
    if population == 0:
        return 0
    jour = 0
    while population > 3**jour:
        jour += 1
    return jour+1

if __name__ == "__main__":
    population = int(input())
    print(contamination(population))
