#########################################
# groupe LDD 5
# Faustine PASSERAT
# Anatole JOORIS
# Clément CRESPIN
# https://github.com/uvsq-info/projet_tas_de_sable
#########################################

#### Import librairies ####

import tkinter as tk
import random as rd


#### CREATION DE LA FENÊTRE ####
racine = tk.Tk()
racine.title("Mon dessin")
WIDTH = 500
HEIGHT = 500


#### CREATION DE LA FONCTION BOUTON ALEATOIRE ####
def aleatoire():
    pass



#### CREATION DU BOUTON ####
bouton_aleatoire = tk.Button(racine, text = "Configuration Aléatoire")

#### CREATION DU CONVAS ####
canvas = tk.Canvas(racine, width = WIDTH, height = HEIGHT, bg = "black")

#### AFFICHAGE ####
bouton_aleatoire.grid(column=1, row = 0)
canvas.grid(column=1, row=1, rowspan = 3)

#### AFFICHAGE DE LA FENÊTRE ####
racine.mainloop()
