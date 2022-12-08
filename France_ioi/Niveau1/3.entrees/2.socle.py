
def volume(largeurSol:int, largeurSup:int):
    return print(sum([i**2 for i in range(largeurSol, largeurSup-1, -1)]))
    


if __name__ == "__main__":
   largeurSol = int(input())
   largeurSup = int(input())
   volume(largeurSol, largeurSup)