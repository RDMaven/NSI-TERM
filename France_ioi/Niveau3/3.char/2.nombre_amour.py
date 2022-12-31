
def nb(prenoms:list):
    
    r = []
    for pre in prenoms:
        print(pre)
        conv_pre = sum([ord(i)-ord("A") for i in pre])
        while conv_pre >= 10:
            conv_pre = sum([int(i) for i in str(conv_pre)])

        r.append(conv_pre)
    
    print(*r)

if __name__ == "__main__":
    prenoms = list(map(str, input().split()))
    nb(prenoms)
