# -*- coding: utf-8 -*-
from math import *
import pygame 

# On implémente ici la formule de Rossmo, qui permet de calculer la probabilité de résidence d'un tueur en série dans une zone géographique en fonction des coordonnées des meurtes déja commis.
# On peut calculer les distances par méthode euclidienne (zones rondes) ou de Manhattan (zones carrées)
# http://www.siteduzero.com/tutoriel-3-422405-profilage-geographique.html


class Killer:
    def __init__(self,f,g,kills=None):
        self.f = f
        self.g = g
        if kills is not None and type(kills).__name__=="list":
            self.kills = kills
        else:
            self.kills = []

    #-------------------#

    def Murder(self,x,y):
        if type(x).__name__=="int" and type(y).__name__=="int":
            self.kills.append((x,y))
        else:
            print "Kill coordinates are integer values"
            
    #-------------------#
            
    def Prob(self,B,H,W):
        # H: height of map
        # W : width of map
        # On recherche ici la probabilité maximum et minimum, pour normaliser les probabilités.
        # On recalculera toutes les probas une 2e fois au lieu de les stocker dans un tableau : trade-off memoire/CPU

        for i in range(H):
            for j in range(W):
                probij = 0
                for crime in range(len(self.kills)):
                    # Calcul de la distance de Manhattan/Euclide (commenter la technique non utilisée. Attention à bien commenter la même dans la fonction ApplyColor(killer,surface) !)
                    #D = Manhattan(i,j,self.kills[crime][0],self.kills[crime][1])
                    D = Euclide(i,j,self.kills[crime][0],self.kills[crime][1])
                    # Si crime hors de la zone tampon
                    if D > B :
                        probij += 1.0/(D**f)
                    # Si crime dans la zone tampon
                    else :
                        probij += float(B)**(self.g-self.f)/((2*B-D)**self.g)

                # Initialisation des pmax/pmin
                if i == 0 and j == 0:
                    biggest = probij
                    smallest = probij

		# Actualisation des pmax/pmin
                if probij > biggest:
                    biggest = probij
                if probij < smallest:
                    smallest = probij

        self.smallest = smallest
        self.biggest = biggest
    
#-------------------#
    
def Manhattan(xi,yi,xn,yn):
    return (abs(xi-xn) + abs(yi-yn))

#-------------------#

def Euclide(xi,yi,xn,yn):
    return sqrt((xi-xn)**2 + (yi-yn)**2)

#-------------------#

def ApplyColor(killer,surface):
    # Calcul des probas pmin/pmax   
    killer.Prob(B,H,W)

    for i in range(W):
        for j in range(H):
            probij = 0
            for crime in range(len(killer.kills)):
                # Calcul de la distance de Manhattan/Euclide 
                #D = Manhattan(i,j,killer.kills[crime][0],killer.kills[crime][1])
                D = Euclide(i,j,killer.kills[crime][0],killer.kills[crime][1])

                 # Si crime hors de la zone tampon
                if D > B :
                    probij += 1/(D**f)
                 # Si crime dans la zone tampon
                else :
                    probij += float(B)**(killer.g-killer.f)/((2*B-D)**killer.g)
            
            probnorm = ceil(((probij-killer.smallest)*100)/(killer.biggest-killer.smallest))
            #Proba comprise entre 0 et 100
            
            #-------PARTITIONNEMENT-------#
            if probnorm >= 0:
                if  probnorm <= 10:
                    surface.set_at((i,j), (0,0,0))# noir
                elif probnorm > 10 and probnorm <= 25:
                    surface.set_at((i,j), (145,139,139))# gris
                elif probnorm > 25 and probnorm <= 40:
                    surface.set_at((i,j), (9,2,80)) # bleu foncé
                elif probnorm > 40 and probnorm <= 55:
                    surface.set_at((i,j), (24,0,255))# bleu 
                elif probnorm > 55 and probnorm <= 70:
                    surface.set_at((i,j), (3,148,71))# vert foncé
                elif probnorm > 70 and probnorm <= 80:
                    surface.set_at((i,j), (5,241,16)) # vert 
                elif probnorm > 80 and probnorm <= 90:
                    surface.set_at((i,j), (195,241,5)) # jaune 
                elif probnorm > 90 and probnorm <= 95:
                    surface.set_at((i,j), (241,155,5)) # orange 
                elif probnorm > 95 and probnorm <= 98:
                    surface.set_at((i,j), (255,0,0)) # rouge
                else:
                    surface.set_at((i,j), (205,10,180))# violet
                    
#-------------------#

def pause():
    running = 1
    while running:                         #Loop this
       for event in pygame.event.get():    #get user input
          if event.type == pygame.QUIT:    #if user clicks the close X
               running = 0                 #make running 0 to break out of loop

#-------------------#


######################
#--------MAIN--------#
######################

# Init-----------------#
W = 638
H = 477

B = 100
f = 0.03
g = 0.1
Meurtres = [(50,300),(300,400),(300,200)]

Dutroux = Killer(f,g,Meurtres)

# Scale Display--------#
print "----------------------------------------------"
print "| Profilage géographique : méthode de Rossmo |"
print "----------------------------------------------\n"
print "#---Echelle colorimetrique---#"
print "Noir :  0 < p < 10"
print "Gris : 10 < p < 25"
print "Bleu foncé : 25 < p < 40"
print "Bleu : 40 < p < 55"
print "Vert foncé : 55 < p < 70"
print "Vert : 70 < p < 80"
print "Jaune : 80 < p < 90"
print "Orange : 90 < p < 95"
print "Rouge : 95 < p < 98"
print "Violet : 98 < p < 100"

# Map Display----------#
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Profilage Géographique - Méthode de Rossmo")
Map = pygame.image.load('Paris.jpg').convert()
screen.blit(Map, (0,0))
pygame.display.flip()

color = pygame.Surface((W,H))

# Proba Calculation----#
ApplyColor(Dutroux,color)

# Color Display--------#
color.set_alpha(150)  

screen.blit(color, (0,0))
pygame.display.flip()

pause()
