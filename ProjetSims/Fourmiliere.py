#! /usr/bin/python3.5
# -*-coding:Utf-8 -*

class Fourmiliere(object):

	def __init__(self, NbReines, NbLarves, NbMales, NbTravailleurs):
		self.ReinesTotales = NbReines
		self.LarvesTotales = NbLarves
		self.MalesTotal = NbMales
		self.TravailleursTotal = NbTravailleurs
		self.PopTotale = self.ReinesTotales + self.LarvesTotales + self.TravailleursTotal + self.MalesTotal

	def AfficherPopulation(self):
		print('Nombre de reines dans la colonie : ' + self.ReinesTotales + '\n')
		print('Nombre de larves dans la colonie : ' + self.LarvesTotales + '\n')
		print('Nombre de males dans la colonie : ' + self.MalesTotal + '\n')
		print('Nombre de travailleurs dans la colonie : ' + self.TravailleursTotal + '\n')
		print('Population totale : ' + self.PopTotale + '\n')




