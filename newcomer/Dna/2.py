import sys
args = sys.argv
dna1 = args[1]
dna2 = args[2]
dna1 = dna1.translate(str.maketrans({'a':'t','t':'a','g':'c','c':'g'}))
if dna1 == dna2: 
    print("yes")
else:
    print("no")
    