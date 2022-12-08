
def calcul_taxe(taxe_actuelle, taxe_nouvelle, prix_legume):
    PHT = prix_legume / (1+(taxe_actuelle/100))
    print(round(PHT*(1+(taxe_nouvelle/100)),2))

if __name__ == "__main__":
    taxe_actuelle = float(input())
    taxe_nouvelle = float(input())
    prix_legume = float(input())
    
    calcul_taxe(taxe_actuelle, taxe_nouvelle, prix_legume)

# x + 5,5*x = 24,9
# x(1+5,5) = 24,9
# x = (24,9)/(1+5,5/100)
# x(1 + 19,6 = ...

# Prix avec taxe = PHT * taux taxe
# 24,9 = x * 5.5
# nouvelle taxe = PHT * taux taxe
# y = 19,6 * x
# y = 19,6 * 24,9 / 5,5
# Prix T.T.C. = Prix H.T. + montant de la TVA
# Prix T.T.C. = Prix H.T. + (Prix Hors Taxes × Taux de TVA)
# 24.9        = x         + x * 5.5/100