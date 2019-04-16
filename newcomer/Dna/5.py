import sys
import re

args = sys.argv
f = open(args[1],'r')

origin = False
dsequence = ""
for line in f:
    if "//" in line:
        break
    if origin == True:
        dsequence += re.sub(r'[0-9]+|\s',"",line)
    if "ORIGIN" in line:
        origin = True
#print(dsequence)

amino = {
        'ttt' : 'F', 'tct' : 'S', 'tat' : 'Y', 'tgt' : 'C',
        'ttc' : 'F', 'tcc' : 'S', 'tac' : 'Y', 'tgc' : 'C',
        'tta' : 'L', 'tca' : 'S', 'taa' : '*', 'tga' : '*',
        'ttg' : 'L', 'tcg' : 'S', 'tag' : '*', 'tgg' : 'W',

        'ctt' : 'L', 'cct' : 'P', 'cat' : 'H', 'cgt' : 'R',
        'ctc' : 'L', 'ccc' : 'P', 'cac' : 'H', 'cgc' : 'R',
        'cta' : 'L', 'cca' : 'P', 'caa' : 'Q', 'cga' : 'R',
        'ctg' : 'L', 'ccg' : 'P', 'cag' : 'Q', 'cgg' : 'R',

        'att' : 'I', 'act' : 'T', 'aat' : 'N', 'agt' : 'S',
        'atc' : 'I', 'acc' : 'T', 'aac' : 'N', 'agc' : 'S',
        'ata' : 'I', 'aca' : 'T', 'aaa' : 'K', 'aga' : 'R',
        'atg' : 'M', 'acg' : 'T', 'aag' : 'K', 'agg' : 'R',

        'gtt' : 'V', 'gct' : 'A', 'gat' : 'D', 'ggt' : 'G',
        'gtc' : 'V', 'gcc' : 'A', 'gac' : 'D', 'ggc' : 'G',
        'gta' : 'V', 'gca' : 'A', 'gaa' : 'E', 'gga' : 'G',
        'gtg' : 'V', 'gcg' : 'A', 'gag' : 'E', 'ggg' : 'G'
}


for i in range(3):
    asequence = ""
    print()
    for j in range(int((len(dsequence)-i)/3)):
        codon = dsequence[i+j*3:i+(j+1)*3]
        asequence += amino[codon]
    print(asequence)