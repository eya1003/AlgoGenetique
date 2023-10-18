import copy
import random


class Individu :
    def __init__(self): 
        self.genome = [ i for i in range(100) ]
        self.variableMutation = 20
        self.fitness = 100
        
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
        resultat = random.randint(0, 1000000)
        if(resultat < self.variableMutation):
            a = random.randint(0,100)
            b = random.randint(0,100)
            gardeA = self.genome[a]
            self.genome[a] = self.genome[b]
            self.genome[b] = gardeA

    def evaluation (self, g, parcours):
        #if len du tabeau si le tableau est pas egale à 100 (moins u plus)
#faire proba totale peut etre ici
        self.fitness = g.getLongueurParcours(parcours)
        penalite = 1000
        if len(self.genome) != 100 or (len(self.genome) != len(set(self.genome))):
            self.fitness += penalite   # a changer : obj - penalités
            print("self.fitness" ,self.fitness)
        return self.fitness