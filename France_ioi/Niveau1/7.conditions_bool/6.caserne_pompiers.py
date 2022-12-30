
def intersect(zones:dict):
    for z in zones.values():
        if bool(set(z[0][0]).intersection(z[1][0])) \
            and bool(set(z[0][1]).intersection(z[1][1])):
            print("OUI")
        else:
            print("NON")

if __name__ == "__main__":
    paires_de_zones = int(input())
    zones = {}
    for i in range(paires_de_zones):
        zones[i] = [[range(int(input()),int(input())) for z in range(2)] for _ in range(2)]
    
    intersect(zones)
