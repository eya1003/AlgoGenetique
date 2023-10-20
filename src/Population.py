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
        self.proba = [individu.fitness/total_fitness for individu in self.population]
        self.proba_totale = 0
        for i in range (len(self.proba)):
            self.proba_totale += self.proba[i]
            
        print("proba: ", self.proba_totale)

    def selection (self): # et peut etre tableau des fitness:
        # uniforme, rang, fitness -> versino tournoi 
        
        numrandom = random.random()
        somme = 0

        for i in range (len(self.population)):
            somme += self.proba[i]
            if (numrandom<=somme):
                return self.population[i]
        
        return  self[random.randint(0, 1000000)]