import re
import sys

#source = open(sys.argv[1],"r")
source = open(sys.argv[1],"r")
destination = open("../files/texteLemTag.csv", "w")
FinalLine = ""
compteur = 0

for line in source :
	word = line.split("\t")[0]
	if len(line.split("\t")) >2:
		tag = line.split("\t")[1]
		lemme = line.split("\t")[2].split("\n")[0]
	#print word + " " + tag + " "+ lemme
	if "EndOfComment" not in line:
		if   tag=="JJ" or  tag=="JJR" or tag=="JJS" or tag=="RB" or tag=="RBR" or tag=="RBS" or tag=="NN" or tag=="NNS" or tag=="VVN":#lemme!="<unknown>":
			if lemme=="<unknown>":
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
