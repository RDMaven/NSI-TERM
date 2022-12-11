def m(metres):
    return "{:f} p".format(metres/0.3048)

def g(grammes):
    return "{:f} l".format(grammes*0.002205)

def c(celcius):
    return "{:f} f".format(32 + 1.8*celcius)

def convertisseur(demandes:dict):
    
    for d in demandes:
        print(eval(d))

       

if __name__ == "__main__":
    nb_conversions = int(input())
    conv = [(c[1] + '(' + c[0] + ')') for c in [input().split() for _ in range(nb_conversions)]]
    #print(conv, sep='\n')
    convertisseur(conv)