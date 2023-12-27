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
        for j in range ( int(100 / 2) ): #penser a mettre 1000000
            p1 = population.selection_fitness_tournois()
            #print(p1.genome)
            p2 = population.selection_fitness_tournois() 
            print("avance")
            (e1, e2) = p1.croisement( p2)
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

################### Tests Celine #####################
'''
def cooldown(temp):
    return (90 * temp) / 100

def TSPUtil(nb_gen):
    # Generation Number
    gen = 1
    # Number of Gene Iterations
    gen_thres = nb_gen

    population = []
    temp = individual()

    # Populating the GNOME pool.
    for i in range(POP_SIZE):
        temp.gnome = create_gnome()
        temp.fitness = cal_fitness(temp.gnome)
        population.append(temp)

    print("\nInitial population: \nGNOME     FITNESS VALUE\n")
    for i in range(POP_SIZE):
        print(population[i].gnome, population[i].fitness)
    print()

    found = False
    temperature = 10000

    # Iteration to perform
    # population crossing and gene mutation.
    while temperature > 1000 and gen <= gen_thres:
        population.sort()
        print("\nCurrent temp: ", temperature)
        new_population = []

        for i in range(POP_SIZE):
            p1 = population[i]

            while True:
                new_g = mutatedGene(p1.gnome)
                new_gnome = individual()
                new_gnome.gnome = new_g
                new_gnome.fitness = cal_fitness(new_gnome.gnome)

                if new_gnome.fitness <= population[i].fitness:
                    new_population.append(new_gnome)
                    break

                else:

                    # Accepting the rejected children at
                    # a possible probability above threshold.
                    prob = pow(
                        2.7,
                        -1
                        * (
                            (float)(new_gnome.fitness - population[i].fitness)
                            / temperature
                        ),
                    )
                    if prob > 0.5:
                        new_population.append(new_gnome)
                        break

        temperature = cooldown(temperature)
        population = new_population
        print("Generation", gen)
        print("GNOME     FITNESS VALUE")

        for i in range(POP_SIZE):
            print(population[i].gnome, population[i].fitness)
        gen += 1'''