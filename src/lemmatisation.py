import re
import sys

source = open(sys.argv[1],"r")
destination = open("../files/texteLematise.csv", "w")
FinalLine = ""
compteur = 0

for line in source :
	word = line.split("\t")[0]
	if len(line.split("\t")) >2:
		tag = line.split("\t")[1]
		lemme = line.split("\t")[2].split("\n")[0]
	#print word + " " + tag + " "+ lemme
	if "EndOfComment" not in line:
			if lemme=="<unknown>" or lemme=="@card@" or lemme=="@ord@":
				lemme = word
				lemme = re.sub(r'[^a-zA-Z0-9]', r'', lemme)
				FinalLine = FinalLine + " " + lemme
			else:
				if FinalLine != "":
						lemme = re.sub(r'[^a-zA-Z0-9]', r'', lemme)
						if len(lemme) > 0:
							FinalLine = FinalLine + " " + lemme
					#print FinalLine
				else :
					FinalLine = lemme
					#print FinalLine
	else:
		destination.write(FinalLine+"\n")
		FinalLine = ""


source.close()
destination.close()
