import random

from Individu import *

class Population :
    def __init__(self):
        self.population = 10000*[Individu]
        for i in range (len(self.population)):
            self.population[i] = Individu()
        #self.population = 1000000*[Individu()]
        self.proba = []
        self.somme_fitness = 0
        self.compteur = 0
        
    def setPopulation(self, tab):
        self.population = tab

    def calcul_proba_fitness ( self ) :
        self.somme_fitness = sum(individu.fitness for individu in self.population)
        self.proba = [(individu.fitness)/self.somme_fitness for individu in self.population]

        #Test Céline
        """total_fitness = sum(1/individu.fitness for individu in self.population)
        self.proba = [(1/individu.fitness)/total_fitness for individu in self.population]"""
        #Fin du test

        """self.proba_totale = 0
        for i in range (len(self.proba)):
            self.proba_totale += self.proba[i]
            
        print("proba: ", self.proba_totale)"""
        

    def selection_random (self): # et peut etre tableau des fitness:
        # uniforme, rang, fitness -> versino tournoi 
        
        numrandom = random.random()
        somme = 0

        for i in range (len(self.population)):
            somme += self.proba[i]
            if (numrandom<=somme):
                return self.population[i]
        
        return  self[random.randint(0, 1000000)]
    
    def selection_par_rang(self):
        # Triez la population en fonction de la fitness
        population_triee = sorted(self.population, key=lambda individu: individu.getFitness())
        
        # Associez un poids de sélection à chaque rang
        poids_rang = [i + 1 for i in range(len(self.population))]
        
        # Effectuez la sélection en fonction des poids de rang
        individu_selectionne = random.choices(population_triee, weights=poids_rang)[0]
        
        return individu_selectionne

    
    def selection_fitness (self):
        #print("proba :", self.calcul_proba())
        
        proba_inverse = [1 - proba for proba in self.proba]     # on avait fait 1/proba
        #proba_inverse.sort(reverse=True)
        proba_totale = sum ( proba_inverse )
        
        numrandom = random.uniform(0, proba_totale)
        #print("proba totale :", proba_totale, "\n")
        #print("random :", numrandom, "\n")
        somme = 0
        for i in range (len(self.population)):
            somme += proba_inverse[i]
            if (numrandom<=somme):
                return self.population[i]
            
    

    
    def selection_fitness_tournois(self):
        proba_inverse = [1-proba for proba in self.proba]
        #proba_inverse.sort(reverse=True)
        proba_totale = sum (proba_inverse)
        self.compteur+=1
        #print("compteur = ", self.compteur)
        #print("proba totale : ", proba_totale)
        #print("proba inverse : ", proba_inverse)

        numrandom = random.uniform(0, proba_totale)
        somme = 0
        candidat = self.population[0]
        
        candidat2 = self.population[0]
        for i in range (len(self.population)):
            somme += proba_inverse[i]
            if (numrandom<=somme):
                candidat = self.population[i]
                break
        #print("candidat 1 : ", candidat.getFitness())
        #print ("candidat original : ", candidat.getFitness())

        for i in range (4):
            #print ("candidat 1:", candidat.getFitness())

            numrandom2 = random.uniform(0, proba_totale)
            #print("proba totale :", proba_totale, "\n")
            #print("random :", numrandom2,)
            somme2 = 0
            for j in range (len(self.population)):
                somme2 += proba_inverse[j]
                if (numrandom2<=somme2):
                    candidat2 = self.population[j]
                    break
            #print("candidat 1 : ", candidat.getFitness())
            #print("candidat 2 : ", candidat2.getFitness(), '\n')

            if (candidat2.getFitness()<=candidat.getFitness()):
                candidat = candidat2
        #print("final : ", candidat.getFitness())
        return candidat