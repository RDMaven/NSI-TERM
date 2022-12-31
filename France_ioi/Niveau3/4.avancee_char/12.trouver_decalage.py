
def trouver_decalage(texte:str):

    texte_copy = texte.lower()
    
    chars = {}
    for i in range(ord("a"), ord("z")+1):
        chars[chr(i)] = texte_copy.count(chr(i))
    
    occ = [(k,v) for k,v in sorted(chars.items(), key=lambda item:item[1], reverse=True)]
    
    #print(chars)
    #print(occ)

    decalage_e = ord('e') - ord(occ[0][0])

    ans = ""

    for char in texte:
        if char.isalpha():
            if char.isupper(): 
                start = ord("A")
            else: 
                start = ord("a")
            char = chr(((ord(char)-start) + decalage_e)%26 + start)
        
        ans += char

    print(ans)


if __name__ == "__main__":
    texte = str(input())

    trouver_decalage(texte)