import copy
import random


class Individu :
    def __init__(self): 
        self.genome = [ i for i in range(100) ]
        random.shuffle(self.genome)
        self.reference =  [ i for i in range(100) ]
        self.variableMutation = 20
        self.fitness = 100
        self.fitness_values = []
        
    def croisement(self, parent2):
        enfant1 = copy.copy(self)
        enfant2 = copy.copy(parent2)
        a = random.randint(0,100)
        b = random.randint(0,100)
        if (a<b):
            for i in range (a, b):
                enfant1.genome[i] = parent2.genome[i]
                enfant2.genome[i] = self.genome[i]
        elif (b<a):
            for i in range (b, a):
                enfant1.genome[i] = parent2.genome[i]
                enfant2.genome[i] = self.genome[i]
        return(enfant1, enfant2)

    def mutation (self):
        #resultat = random.randint(0, 1000000)
        resultat = random.randint(0, 100)
        #print("résultat = ", resultat)
        if(resultat < self.variableMutation):
            a = random.randint(0,99)
            b = random.randint(0,99)
            gardeA = self.genome[a]
            self.genome[a] = self.genome[b]
            self.genome[b] = gardeA
            
            
    def evaluation(self, g):
        fitness = g.getLongueurParcours(self.genome)
        penalite = 1000
        total_penalites = 0
        #print(fitness)

        if len(self.genome) != 100:
            total_penalites += penalite
            print("Pénalité ajoutée pour la longueur du génome")

        if len(self.genome) != len(set(self.genome)):
            num_duplicates = len(self.genome) - len(set(self.genome))
            total_penalites += num_duplicates * penalite
            #print(f"Pénalité ajoutée pour {num_duplicates} doublons")

        # Liste de tous les chiffres de 0 à 99
        #chiffres_specifiques = list(range(100))

        fitness += total_penalites
        self.fitness = fitness
        

        return fitness
    
    def getFitness(self):
        return self.fitness