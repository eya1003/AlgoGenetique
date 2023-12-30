import sys
from Population import *
from core.Region import Region
from core.Ville import Ville
from core.Graphe import Graphe

def main (graphe, r, nb_generations):
    population = Population()
    
    for i in range (nb_generations) :
        
        #print("truc")
        # je pense que la fitness doit être calculée ici
        fitness_values = []
        
        for individu in population.population:
            fit = individu.evaluation(graphe)
            
            # Stocker la fitness de cet individu dans la liste
            fitness_values.append(fit)
            #print(f"Fitness après ajout de pénalités : {fit}")

        #print("fitness values", fitness_values)
        population.calcul_proba_fitness()

        populationEnfants = []
        for j in range ( int(10000 / 2) ): #penser a mettre 1000000
            p1 = population.selection_fitness_tournois()
            #print(p1.genome)
            p2 = population.selection_fitness_tournois() 
            #print(p2.genome)
            (e1, e2) = p1.croisement_avec_correction_et_trajet(p1,p2)
            e1.mutation ()
            e2.mutation()
            populationEnfants.append(e1)
            populationEnfants.append(e2)
            # afficher les villes dans le tableau

        population.setPopulation(populationEnfants)
        

    # Obtenez le meilleur individu de la population
    print("Meilleur parcours")
    meilleur_fit = 100000000
    meilleur_individu = population.population[0]
    for individu in population.population:
        fit = individu.evaluation(graphe)
        if (fit<meilleur_fit):
            meilleur_fit = fit
            meilleur_individu = individu

    meilleur_parcours = meilleur_individu.genome
    print("getfit: ", meilleur_individu.getFitness())
    print("distance : ", graphe.getLongueurParcours(meilleur_parcours))

    # Affichez les villes que le parcours prend
    villes_du_parcours = [r.getVilles()[i].getNumero() for i in meilleur_parcours]

    print("Le meilleur parcours prend les villes dans l'ordre suivant:", villes_du_parcours)

    return meilleur_parcours

#if __name__ == '__main__' :
#   sys.exit(main())