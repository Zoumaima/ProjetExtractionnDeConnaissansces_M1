# -*- coding: utf-8 -*-
import os
import sys

"""
	Deuxième partie :
	Transformation de ce fichier csv en arff
"""
# L'option -S "i-j" signifie que les ieme jusqu'à jeme attributs sont des strings
# L'option -L "i-j:A,...,Z" signifie que les ieme jusqu'à jeme attributs sont nominals
# c'est à dire prenent des valeurs dans l'ensemble donné {A,...,Z}
os.system("java -cp ./weka.jar   weka.core.converters.CSVLoader "+sys.argv[1]+" -S \"1-1\" -L \"2-2\":-1,1  > ../files/"+sys.argv[2]+"")

	
