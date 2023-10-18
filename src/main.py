import sys
from Population import *
from core.Region import Region
from core.Ville import Ville
from core.Graphe import Graphe

def main (graphe):
    population = Population()
    populationEnfants = []
    for i in range (10) :
        print("truc")
        for individu in population.population:
            fit = individu.evaluation()

        population.calcul_proba()

        for j in range ( int(100 / 2) ): #penser a mettre 1000000
            p1 = population.selection ()
            p2 = population.selection () 
            (e1, e2) = p1.croisement( p2)
            e1.mutation ()
            e2.mutation()
            populationEnfants.append(e1)
            populationEnfants.append(e2)
            # afficher les villes dans le tableau
        
        population.setPopulation(populationEnfants)
        
    return population.population[0].genome

#if __name__ == '__main__' :
 #   sys.exit(main())