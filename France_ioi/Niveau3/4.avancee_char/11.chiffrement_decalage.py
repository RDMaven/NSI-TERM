
def decryptage(nbPages, textes:list[str]):
    for i in range(nbPages-1):
        noPage = 2 + i
        if noPage%2 == 0:
            decalage = - 3*noPage
        else:
            decalage = 5*noPage

        ans = ""

        for char in textes[i]:
            if char.isalpha():
                if char.isupper():
                    start = ord("A")
                else:
                    start = ord("a")
                
                pos_char = ord(char)-start # a:0, z:25
                nv_char = chr((pos_char + decalage)%26 + start)
                ans += nv_char
            
            else:
                ans += char

        print(ans)


if __name__ == "__main__":
    nbPages = int(input())
    textes = [str(input()) for _ in range(nbPages-1)]

    decryptage(nbPages, textes)