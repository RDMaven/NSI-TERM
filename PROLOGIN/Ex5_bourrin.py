
# Function to print all distinct combinations of length `k`
def findCombinations(A:list, k:int, subarrays:list, out=(), i=0):
 
    # invalid input
    if len(A) == 0 or k > len(A):
        return
 
    # base case: combination size is `k`
    if k == 0:
        #print(f"#######==> {out}")
        subarrays.append(out)
        return
 
    # start from the next index till the last index
    for j in range(i, len(A)):
        # add current element `A[j]` to the solution and recur for next index
        # `j+1` with one less element `k-1`
        #print(j, out, A[j])
        findCombinations(A, k - 1, subarrays, out + (A[j],), j + 4)

"""subarrays= list() 
findCombinations(['0:3','1:4','2:5','3:6', '4:7', '5:8', '6:9', '7:10', '8:11', '9:12'], 3, subarrays)
print(subarrays)
"""


def stabilite_maximale(n: int, k: int, p: int, accroches: list[int]) -> None:
    """
    :param n: nombre d'accroches
    :param k: nombre de stabilisateurs
    :param p: indice de stabilité parfaite
    :param accroches: hauteur de chaque accroche
    """

    k = k if n//4 >= k else n//4

    #trier la liste des accroches
    accroches.sort()

    if n < 4: #on ne peut rien stabiliser
        return print(0)

    else: 
        deltas = []
        appender = deltas.append
        diffs = []
        di_ap = diffs.append
    
        for i in range(n-3):
            diff2 = p - (accroches[i+3]-accroches[i])**2
            diff = accroches[i:i+4]

            appender(diff)
            di_ap(diff2)
            
    print("======")
    print(deltas)


    list_combinations = list()
    results = list()

    for n in range(k + 1):
        subarrays = []
        findCombinations(deltas, n, subarrays=subarrays)
        list_combinations += subarrays
        sub2 = list()
        findCombinations(diffs, n, subarrays=sub2)
        results += sub2

    print(list_combinations)
    print([sum(a) for a in results])

    """
    [[1, 2, 3, 4], [2, 3, 4, 4], [3, 4, 4, 4], [4, 4, 4, 5], [4, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 9]]
    [[0], [1], [2], [3], [4], [5], [6]]
    
    [0] : \ [1], [2], [3]                   ==> range(i+3+1)
    [1] : \ [0], [2], [3], [4]              ==> range(i-3, i+3+1)
    [2] : \ [0], [1], [3], [4], [5]
    [3] : \ [0], [1], [2], [4], [5], [6]

    """

    return print(0)
    
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = list(map(int, input().split()))
    stabilite_maximale(n, k, p, accroches)
    
