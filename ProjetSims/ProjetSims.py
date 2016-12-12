#! /usr/bin/python3.5
# -*-coding:Utf-8 -*

from Fourmiliere import *
from Larve import *
from Reine import *
from Travailleur import *
from Male import *

class Main:
	ID = 0

print('Indiquez le nombre de reines que vous souhaitez creer \n')
NbReines = input()
print('Indiquez le nombre de larves que vous souhaitez creer \n')
NbLarves = input()
print('Indiquez le nombre de males que vous souhaitez creer \n')
NbMales = input()
print('Indiquez le nombre de travailleurs que vous souhaitez creer \n')
NbTravailleurs = input()

fourmiliere = Fourmiliere(NbReines, NbLarves, NbMales, NbTravailleurs)
reine = Reine(Main.ID)
input()
fourmiliere.AfficherPopulation()
input()
reine.Pondre()
input()
fourmiliere.AfficherPopulation()
input()