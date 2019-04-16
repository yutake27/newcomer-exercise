import sys
args = sys.argv
dna = args[1]
print(dna.translate(str.maketrans({'a':'t','t':'a','g':'c','c':'g'})))