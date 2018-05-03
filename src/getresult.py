import re
import os
import sys

source = open(sys.argv[1],"r")
destination = open("resultat.csv", "w")

for line in source :
	prediction = line.split(",")[2]
	destination.write(prediction+"\n")



source.close()
destination.close()

source = open("./resultat.csv","r")
destination = open("resultatFinal.csv", "w")

for line in source :
	prediction = line.split(":")[1]
	destination.write(prediction)

os.remove("resultat.csv")

source.close()
destination.close()
