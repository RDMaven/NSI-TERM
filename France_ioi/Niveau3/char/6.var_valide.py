
def valide(nomVar:list[str]):

    def is_alpha_(char):
        return ("a" <= char and char <= "z") or ("A" <= char and char <= "Z") or (char == '_')

    for variable in nomVar:
        #print(f"testing VARIABLE = {variable}")
        if is_alpha_(variable[0]):
            #print(f"first is alpha : {variable[0]}")
            i = 1
            go = True
            while i <= len(variable)-1 and go == True:
                #print(f"{variable[i]} : {(variable[i].isdigit() or is_alpha_(variable[i]))}")
                if not (variable[i].isdigit() or is_alpha_(variable[i])):
                    go = False
                i += 1
            print("YES" if go else "NO")
        else:
            print("NO")


if __name__ == "__main__":

   nbNoms = int(input())
   nomVar = [str(input()) for _ in range(nbNoms)]
   valide(nomVar)   
