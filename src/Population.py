import random

from Individu import *

class Population :
    def __init__(self):
        self.population = 100*[Individu]
        for i in range (len(self.population)):
            self.population[i] = Individu()
        #self.population = 1000000*[Individu()]
        self.proba = []
        
    def setPopulation(self, tab):
        self.population = tab

    def calcul_proba ( self ) :
        total_fitness = sum(individu.fitness for individu in self.population)
        self.proba = [(individu.fitness)/total_fitness for individu in self.population]
        return self.proba
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
    
    def selection_fitness (self):
        #print("proba :", self.calcul_proba())
        
        proba_inverse = [1/proba for proba in self.calcul_proba()]
        proba_inverse.sort(reverse=True)
        proba_totale = 0
        for i in range (len(proba_inverse)):
            proba_totale += proba_inverse[i]
        
        numrandom = random.uniform(0, proba_totale)
        print("proba totale :", proba_totale, "\n")
        print("random :", numrandom, "\n")
        somme = 0
        for i in range (len(self.population)):
            somme += proba_inverse[i]
            if (numrandom<=somme):
                return self.population[i]