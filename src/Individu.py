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
    
    def croisement_permut_decal(self, parent2):
        #   voir pour le stack overflow du compteur et de parent2.genome[compteur1] --> le parent2 ne change pas
        enfant1 = copy.deepcopy(self)
        enfant2 = copy.deepcopy(parent2)
        verif1 = 0
        verif2 = 0
        garderval1 = []
        garderval2 = []
        a = random.randint(0,99)
        b = random.randint(0,99)
        
        for i in range (100):
            if not(i in enfant1.genome) :
                for j in range (100):
                    if (enfant1.genome.count(j)>1):
                        enfant1.genome[enfant1.genome.index(j)] = i
            if not(i in enfant2.genome) :
                for j in range (100):
                    if (enfant1.genome.count(j)>1):
                        enfant1.genome[enfant1.genome.index(j)] = i

        if (a<b):
            compteur1 = b
            compteur2 = b
            for i in range (a, b):
                parent2mem = parent2.genome[i]
                parent1mem = self.genome[i]
                enfant1.genome[i] = parent2mem
                garderval1.append(parent2mem)
                enfant2.genome[i] = parent1mem
                garderval2.append(parent1mem)

            for i in range (b, len(enfant1.genome)):
                
                while (self.genome[compteur1] in garderval1):
                    # print("parent 1 : ", parent2.genome[compteur1])
                    # print("valeur 1 : ", garderval1)
                    # # print("compteur 1 : ", compteur1)
                    if (compteur1+1<len(enfant1.genome)):
                        compteur1+=1
                    else:
                        compteur1=0
                enfant1.genome[i] = self.genome[compteur1]
                garderval1.append(self.genome[compteur1])

                while (parent2.genome[compteur2] in garderval2):
                    # print("parent 2 : ", self.genome[compteur2])
                    # print("valeur 2 : ", garderval2)
                    #print("compteur 2 : ", compteur2)
                    if (compteur2+1<len(enfant2.genome)):
                        compteur2+=1
                    else:
                        compteur2=0
                enfant2.genome[i] = parent2.genome[compteur2]
                garderval2.append(parent2.genome[compteur2])

                if (compteur1+1<len(enfant1.genome)):
                    compteur1+=1
                else:
                    compteur1=0
                if (compteur2+1<len(enfant2.genome)):
                    compteur2+=1
                else:
                    compteur2=0

            for i in range (a):
                while (self.genome[compteur1] in garderval1):
                    # print("parent 1 : ", parent2.genome[compteur1])
                    # print("valeur 1 : ", garderval1)
                    ## print("compteur 1 : ", compteur1)
                    if (compteur1+1<len(enfant1.genome)):
                        compteur1+=1
                    else:
                        compteur1=0
                enfant1.genome[i] = self.genome[compteur1]
                garderval1.append(self.genome[compteur1])

                while (parent2.genome[compteur2] in garderval2):
                    # print("parent 2 : ", parent2.genome[compteur2])
                    # print("valeur 2 : ", garderval2)
                    ## print("compteur 2 : ", compteur2)
                    if (compteur2+1<len(enfant2.genome)):
                        compteur2+=1
                    else:
                        compteur2=0
                enfant2.genome[i] = parent2.genome[compteur2]
                garderval2.append(parent2.genome[compteur2])

                if (compteur1+1<len(enfant1.genome)):
                    compteur1+=1
                else:
                    compteur1=0
                if (compteur2+1<len(enfant2.genome)):
                    compteur2+=1
                else:
                    compteur2=0
                
        elif (b<a):
            compteur1 = a
            compteur2 = a
            for i in range (b, a):
                parent2mem = parent2.genome[i]
                parent1mem = self.genome[i]
                enfant1.genome[i] = parent2mem
                garderval1.append(parent2mem)
                enfant2.genome[i] = parent1mem
                garderval2.append(parent1mem)

            for i in range (a, len(enfant1.genome)):
                
                while (self.genome[compteur1] in garderval1):
                    # print("parent 1 : ", self.genome[compteur1])
                    # print("valeur 1 : ", garderval1)
                    if (compteur1+1<len(enfant1.genome)):
                        compteur1+=1
                    else:
                        compteur1=0
                enfant1.genome[i] = self.genome[compteur1]
                garderval1.append(self.genome[compteur1])

                while (parent2.genome[compteur2] in garderval2):
                    # print("parent 2 : ", parent2.genome[compteur2])
                    # print("valeur 2 : ", garderval2)
                    if (compteur2+1<len(enfant2.genome)):
                        compteur2+=1
                    else:
                        compteur2=0
                enfant2.genome[i] = parent2.genome[compteur2]
                garderval2.append(self.genome[compteur2])

                if (compteur1+1<len(enfant1.genome)):
                    compteur1+=1
                else:
                    compteur1=0
                if (compteur2+1<len(enfant2.genome)):
                    compteur2+=1
                else:
                    compteur2=0

            for i in range (b):
                while (self.genome[compteur1] in garderval1):
                    # print("parent 1 : ", self.genome[compteur2])
                    # print("valeur 1 : ", garderval1)
                    if (compteur1+1<len(enfant1.genome)):
                        compteur1+=1
                    else:
                        compteur1=0
                enfant1.genome[i] = self.genome[compteur1]
                garderval1.append(self.genome[compteur1])

                while (parent2.genome[compteur2] in garderval2):
                    # print("parent 2 : ", parent2.genome[compteur2])
                    # print("valeur 2 : ", garderval2)
                    if (compteur2+1<len(enfant2.genome)):
                        compteur2+=1
                    else:
                        compteur2=0
                enfant2.genome[i] = parent2.genome[compteur2]
                garderval2.append(parent2.genome[compteur2])

                if (compteur1+1<len(enfant1.genome)):
                    compteur1+=1
                else:
                    compteur1=0
                if (compteur2+1<len(enfant2.genome)):
                    compteur2+=1
                else:
                    compteur2=0

        return(enfant1, enfant2)
    #test_eya
    def croisement_multipoints(self, parent2):
        
        enfant1 = copy.deepcopy(self)
        enfant2 = copy.deepcopy(parent2)

        # Définir plusieurs points de croisement
        points_de_croisement = sorted(random.sample(range(1, 99), 3))

        # Initialiser les indices de début et de fin pour le premier segment
        start_index = 0
        end_index = points_de_croisement[0]

        # Effectuer le croisement en alternant les segments
        for point in points_de_croisement:
            if start_index % 2 == 0:
                enfant1.genome[start_index:end_index] = parent2.genome[start_index:end_index]
                enfant2.genome[start_index:end_index] = self.genome[start_index:end_index]
            else:
                enfant1.genome[start_index:end_index] = self.genome[start_index:end_index]
                enfant2.genome[start_index:end_index] = parent2.genome[start_index:end_index]

            # Mettre à jour les indices de début et de fin pour le prochain segment
            start_index = end_index
            end_index = point

        # Effectuer le dernier segment
        if start_index % 2 == 0:
            enfant1.genome[start_index:] = parent2.genome[start_index:]
            enfant2.genome[start_index:] = self.genome[start_index:]
        else:
            enfant1.genome[start_index:] = self.genome[start_index:]
            enfant2.genome[start_index:] = parent2.genome[start_index:]


        return enfant1, enfant2

    def croisement_avec_correction_et_trajet(self, parent1, parent2):
        debut = random.randint(1, len(parent1.genome) - 1)

        enfant1_genome = parent1.genome[:debut] + parent2.genome[debut:]
        
        
        enfant2_genome = parent2.genome[:debut] + parent1.genome[debut:]
        enfant1 = self.create_and_correct_individual(enfant1_genome)
        enfant2 = self.create_and_correct_individual(enfant2_genome)


        return enfant1, enfant2

    def create_and_correct_individual(self, genome):
        individu = Individu()
        individu.genome = self.distance_calcul(genome)
        return individu

    def distance_calcul(self, trajet):

        final_ville = []
        tab_villes= set()
        for ville in trajet:
            if ville not in tab_villes:
                final_ville.append(ville)
                tab_villes.add(ville)
        ajout = set(range(len(trajet))) - tab_villes
        final_ville.extend(ajout)

        return final_ville

    
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