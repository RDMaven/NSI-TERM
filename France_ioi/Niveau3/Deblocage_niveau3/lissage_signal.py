def passage(nbMesures:int, diffMax:int, mesures:list):
    
    if nbMesures <= 2:
        return 0
    
    #print("\033[32;1m")
    #print(f"0 {mesures}\033[0m")
    
    initVerif = all([(abs(mesures[m-1]-mesures[m]) <= diffMax) for m in range(1, nbMesures)])
    if initVerif:
        return 0

    total_lissages = 0
    relisser = True

    
    while relisser == True:
        relisser = False
        total_lissages += 1
        
        mesures_lissage = mesures.copy()
    
        for m in range(1, nbMesures-1):
            mesures_lissage[m] = (mesures[m-1]+mesures[m+1])/2
            #pr_m = ["{:f}".format(i) for i in mesures_lissage]
            #pr_m[m] = f"\033[32;1m{pr_m[m]}\033[0m"
            #print(*pr_m)

            #print(f"\033[33m{diffMax, round(abs(mesures_lissage[m-1]-mesures_lissage[m]), 6)}\033[0m")
            if relisser == False:

                if m == nbMesures-2:
                    if abs(mesures_lissage[m+1]-mesures_lissage[m]) > diffMax:
                        relisser = True
                
                if (abs(mesures_lissage[m-1]-mesures_lissage[m]) > diffMax):
                    relisser = True
                #print(f"\033[31m{True}\033[0m")
            
        #print('\033[36m', total_lissages, mesures_lissage, "\033[0m")
        mesures = mesures_lissage.copy()

    #print(mesures_lissage)
    return total_lissages
    
if __name__ == "__main__":
    nbMesures = int(input())
    diffMax = float(input())
    mesures = [float(input()) for _ in range(nbMesures)]

    print(passage(nbMesures,diffMax,mesures))