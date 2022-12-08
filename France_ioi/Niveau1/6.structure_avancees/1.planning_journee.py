
def villages_proches(position:int, nombre_villages, position_villages:list):
    print(len([position-position_villages[i] for i in range(nombre_villages) if position-position_villages[i] in range(-50,50+1)]))


if __name__ == "__main__":
    position = int(input())
    nombre_villages = int(input())
    position_villages = [int(input()) for _ in range(nombre_villages)]
    villages_proches(position, nombre_villages, position_villages)

"""


"""