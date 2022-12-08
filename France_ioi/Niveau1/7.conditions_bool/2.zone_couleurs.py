
def sur_plan(jetons:list):
    
    def zone_jeu(jeton:list):
        if not ((jeton[0] in range(0,90)) and (jeton[1] in range(0,70))):
            print("En dehors de la feuille")
            return False
        return True
    
    def zone_jaune_centre(jeton:list):
        if ((jeton[0] in range(25,50)) and (jeton[1] in range(20,45))):
            print("Dans une zone jaune")
            return True
        return False

    def zone_bleue(jeton:list):
        if ((jeton[0] in range(10,85)) and (jeton[1] in range(10,55))) and not zone_jaune_centre(jeton):
            print("Dans une zone bleue")
            return True
        return False
        
    def zones_rouges(jeton:list):
        if (jeton[1] in range(60,70)) and ((jeton[0] in range(15,45)) or (jeton[0] in range(60,85))):
            print("Dans une zone rouge")
            return True
        return False

    def zone_jaune(jeton:list):
        if not (zone_bleue(jeton) or zones_rouges(jeton)):
            print("Dans une zone jaune")
            return True
        return False

    for jeton in jetons:
        if not ((jeton[0] in range(0,90)) and (jeton[1] in range(0,70))):
            print("En dehors de la feuille")
        
        else:
            if (jeton[1] in range(60,70)) and ((jeton[0] in range(15,45)) or (jeton[0] in range(60,85))):
                print("Dans une zone rouge")
            elif ((jeton[0] in range(10,85)) and (jeton[1] in range(10,55))) and not ((jeton[0] in range(25,50)) and (jeton[1] in range(20,45))):
                print("Dans une zone bleue")
            else:
                print("Dans une zone jaune")
      


if __name__ == "__main__":
    nb_jetons = int(input())
    jetons = []
    for i in range(nb_jetons):
        jetons.append([int(input()) for _ in range(2)])
    
    sur_plan(jetons)