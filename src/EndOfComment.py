import sys

doc = open(sys.argv[1],"r")

destination = open("../files/DataWithEndOfComment.csv", "w")

for ligne in doc :
    ligne=ligne+"EndOfComment\n"
    print(ligne)
    destination.write(ligne)
