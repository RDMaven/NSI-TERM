
def frequence(phrase:str):

    phrase = ''.join(filter(str.isalpha, phrase.lower()))
    nb_lettres = len(phrase)

    for l in range(ord('a'), ord('z')+1):
        counted = phrase.count(chr(l))
        #print("{0:} {1:f} {2:}".format(chr(l), counted/nb_lettres, counted))
        print("{:f}".format(counted/nb_lettres))


if __name__ == "__main__":

   phrase = str(input())
   frequence(phrase)   
