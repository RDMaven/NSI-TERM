
def pyramidation(max_pierres:int):
    prev = (0,0)

    pierres_pyramide=0
    p = 0
    
    while pierres_pyramide <= max_pierres:
        prev = (p-1, pierres_pyramide)
        pierres_pyramide = (p*(p+1)*((2*p)+1))//6
        p += 1
    
    print(*prev, sep="\n")
    

if __name__ == "__main__":
    max_pierres = int(input())
    pyramidation(max_pierres)
    
    