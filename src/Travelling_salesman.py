from core.Region import *
from core.Graphe import *
from gui.MainWindow import *
from main import *

# Paramètres du problème
w = 800
h = 600
nb_villes = 100

# Génération du problème
r = Region ( w, h, nb_villes )

# Graphe du problème
g = Graphe ( r, nb_villes )

# Insérer votre code ici
g.setBestParcours([0,1,2])
chemin = main(g, r, 5)
g.setBestParcours ( chemin )

# eya essaie d'afficher des informations du ville
ville_visitees= []
for i in chemin:
    #afficher pour chaque ville son abscisse , ordonne et numero
    ville = g.region.getVilles()[i]
    abscisse= ville.getAbscisse()
    ordonne = ville.getOrdonnee()
    numero = ville.getNumero()
    #print(abscisse, ordonne, numero)
    #if i in ville_visitees:
    #   print(f"Ville {i} est dupliquée")
    #else:
    #    ville_visitees.append(i)



# Affichage du résultat
print ( "Distance finale :", int(g.getLongueurParcours(g.getBestParcours())), "kilomètres" )
fenetre = MainWindow( r, g )
fenetre.loop()
