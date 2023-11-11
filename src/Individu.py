import copy
import random
import math


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
        """a = random.randint(0,99)
        b = random.randint(0,99)
        if (a<b):
            for i in range (a, b):
                enfant1.genome[i] = parent2.genome[i]
                enfant2.genome[i] = self.genome[i]
        elif (b<a):
            for i in range (b, a):
                enfant1.genome[i] = parent2.genome[i]
                enfant2.genome[i] = self.genome[i]"""
        
        for i in range (10):
            echange = random.randint(0, 99)
            v1 = enfant1.genome[echange]
            v2 = enfant2.genome[echange]
            
            for j in range (len(enfant1.genome)):
                if (enfant1.genome[j] == v2):
                    enfant1.genome[echange] = enfant1.genome[j]
                    enfant1.genome[j] = v1
                break

            for j in range (len(enfant1.genome)):       
                if (enfant2.genome[j] == v1):
                    enfant2.genome[echange] = enfant2.genome[j]
                    enfant2.genome[j] = v2
                break
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
            
    def mutation_echange_deux_genes(self):
        resultat = random.randint(0, 100)
        if resultat < self.variableMutation:
            a, b = random.sample(range(100), 2)
            gardeA = self.genome[a]
            self.genome[a] = self.genome[b]
            self.genome[b] = gardeA
            
    def mutation_deplacement(self):
        resultat = random.randint(0, 100)
        if resultat < self.variableMutation:
            index1, index2 = random.sample(range(100), 2)
            gene_a_deplacer = self.genome.pop(index1)
            self.genome.insert(index2, gene_a_deplacer)


            
    def evaluation(self, g):
        fitness = g.getLongueurParcours(self.genome)
        penalite = 1000
        total_penalites = 0
        #print(fitness)

        if len(self.genome) != 100:
            total_penalites += penalite
            #print("Pénalité ajoutée pour la longueur du génome")

        """if len(self.genome) != len(set(self.genome)):
            num_duplicates = len(self.genome) - len(set(self.genome))
            total_penalites += num_duplicates * penalite
            #print(f"Pénalité ajoutée pour {num_duplicates} doublons")"""
        
        #test Céline
        if len(self.genome) != len(set(self.genome)):
            num_duplicates = len(self.genome) - len(set(self.genome))
            total_penalites += (num_duplicates * penalite) + math.exp( num_duplicates )


        # Liste de tous les chiffres de 0 à 99
        #chiffres_specifiques = list(range(100))

        fitness += total_penalites
        self.fitness = fitness
        

        return fitness
    
    def getFitness(self):
        return self.fitness