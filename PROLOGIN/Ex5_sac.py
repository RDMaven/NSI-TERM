def knapsack(n, p, k, values):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    print(dp)
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j >= 1:
                dp[i][j] = dp[i-1][j]
                if values[i-1] <= j:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + values[i-1])

    res = 0
    for i in range(1, k+1):
        res = max(res, dp[n][i] - (i * p - i * i))

    return res

"""
Cet algorithme utilise une matrice de programmation dynamique dp pour stocker les résultats partiels. Le temps d'exécution de cet algorithme est en O(n*k), où n est la taille de la liste de valeurs et k est la valeur de la limite de sélection.

La fonction prend en entrée les paramètres n, p, k et values, où n est la taille de la liste de valeurs, p est la valeur donnée, k est la limite de sélection, et values est la liste de valeurs à utiliser pour le calcul. La fonction renvoie le résultat optimal du calcul.

A remarquer, qu'on utilise dans l'algorithme la formule (q * p - somme de chaque valeur au carré) pour maximiser la fonction, c'est l'objectif a atteindre.
"""

def stabilite_maximale(n, k, p, accroches):
    knapsack(n, p, k, accroches)


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = sorted(list(map(int, input().split())))
    stabilite_maximale(n, k, p, accroches)
    