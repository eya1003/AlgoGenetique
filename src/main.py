import sys
from Population import *
from core.Region import Region
from core.Ville import Ville
from core.Graphe import Graphe

def main (graphe, r):
    population = Population()
    populationEnfants = []
    for i in range (1) :
        #print("truc")
        population.calcul_proba()
        
        for j in range ( int(2 / 2) ): #penser a mettre 1000000
            p1 = population.selection ()
            #print(p1.genome)
            p2 = population.selection () 
            print("avant P1: ", p1.genome)
            print("avant P2: ",p2.genome)
            (e1, e2) = p1.croisement( p2)
            print("après E1: ",e1.genome)
            print("après E2: ",e1.genome)
            e1.mutation ()
            e2.mutation()
            populationEnfants.append(e1)
            populationEnfants.append(e2)
            # afficher les villes dans le tableau

        population.setPopulation(populationEnfants)
        
        for individu in population.population:
            parcours = individu.genome
            fit = individu.evaluation(graphe, parcours)
            
    #Laya essaye quelque chose :
    # Obtenez le meilleur individu de la population
    meilleur_individu = population.population[0]
    meilleur_parcours = meilleur_individu.genome

    # Affichez les villes que le parcours prend
    villes_du_parcours = [r.getVilles()[i] for i in meilleur_parcours]

    print("Le meilleur parcours prend les villes dans l'ordre suivant:")
    """for ville in villes_du_parcours:
        print(ville)"""
        
    ### fin du test de Laya
    return population.population[0].genome

#if __name__ == '__main__' :
#   sys.exit(main())