# -*- coding: utf-8 -*-
import os, re
import sys


data = open(sys.argv[1],"r")
labels = open(sys.argv[2],"r")
combinaison = open("../files/"+sys.argv[3],"w")
print("\n")
t = data.readline().split("\n")[0]
l = labels.readline()

combinaison.write("Comments,Labels\n")

while t and l:
	#Je dois mettre le texte entre guillement et enlever les virgules du texte
	#car pour transformer en arff, weka veut que le texte soit entre guillemets dans le fichier csv
	#et le fichier csv est mal parsé si il y a des virgules en plein milieu du texte
	combinaison.write("\""+t.replace("\"","'")+"\""+","+l)
	#Je dois aussi enlever le retour a la ligne à la fin du texte, curieusement je n'ai pas ce probleme avec les labels
	t = data.readline().split("\n")[0]
	l = labels.readline()

data.close()
labels.close()
combinaison.close()
