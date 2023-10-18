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
chemin = main()


g.setBestParcours ( chemin )

# Affichage du résultat
print ( "Distance finale :", int(g.getLongueurParcours(g.getBestParcours())), "kilomètres" )
fenetre = MainWindow( r, g )
fenetre.loop()
