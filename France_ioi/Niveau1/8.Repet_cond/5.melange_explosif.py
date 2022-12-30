
def analyse_danger(mesures, temp_min, temp_max, total_mesures):
    i = 0
    
    while mesures[i] in range(temp_min, temp_max+1):
        print("Rien à signaler")
        if i < total_mesures-1:
            i +=1
        else:
            return
    print("Alerte !!")

if __name__ == "__main__":
    total_mesures = int(input())
    temp_min = int(input())
    temp_max = int(input())
    mesures = [int(input()) for _ in range(total_mesures)]
    
    analyse_danger(mesures, temp_min, temp_max, total_mesures)
