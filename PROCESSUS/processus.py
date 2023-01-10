# P4
class Processus:
    def __init__(self, nom, duree, priorite):
        self.nom = nom
        self.priorite = priorite
        self.chrono = 0
        self.duree = duree
        self.etat = 'eligible'       
    def __str__(self):
        return f"{self.nom}: {self.etat}" 
    def execute(self) :
        self.etat = 'elu'
        self.chrono += 1 
    def eligible(self):
        self.etat = 'eligible'


if __name__ == "__main__":

    # P0 : On donne la liste de processus suivant
    liste_processus = [[f'P{i}_tache_{n}' for n in range(1, j+1)] for i,j in [(1,7), (2,3), (3,5)]]

    liste_processus = [
    # Processus 1
            ["P1_tache_1",
            "P1_tache_2",
            "P1_tache_3",
            "P1_tache_4",
            "P1_tache_5",
            "P1_tache_6",
            "P1_tache_7"],
    # Processus 2
            ["P2_tache_1",
            "P2_tache_2",
            "P2_tache_3"],
    # Processus 3
            ["P3_tache_1",
            "P3_tache_2",
            "P3_tache_3",
            "P3_tache_4",
            "P3_tache_5"]]

    length = len(liste_processus)
    sorted_liste = sorted(liste_processus, key=len)
    

    # P1 : Premier arrivé, premier servi, FCFS (First Come, First Served)
    print("Ordonnancement des instructions exécutées par le microprocesseur :")
    process_FCFS = [i for j in liste_processus for i in j]
    print(process_FCFS)

    # P2 : Plus court d'abord, SJF (Shortest Job First)
    print("Ordonnancement des instructions exécutées par le microprocesseur :")
    process_SJF = [i for j in sorted_liste for i in j]
    print(process_SJF)

    # p3 : Le tourniquet, RR (Round Robin)
    print("Ordonnancement des instructions exécutées par le microprocesseur :")
    process_RR = [liste_processus[i][j] for j in range(len(sorted_liste[-1])) for i in range(length) if j in range(len(liste_processus[i]))]
    print(process_RR)
    
    # p4 : avec priorités:
    processus_prio = [(1, 0,3,3), (2, 1,6,2), (3, 4,4,1), (4, 6,2,4), (5, 7,1,5)]
    
    temps = 0
    lprocesseurs = [Processus('P1', 3, 3)]
    processus_prio.pop()
    process_append = lprocesseurs.append
    zombies = []
    priority = [0, 3]

    while len(lprocesseurs):
        for p in processus_prio:
            if temps == p[1]:
                process_append(Processus(f'P{p[0]}', p[2], p[3]))
        
        
        temps += 1