import sys

args = sys.argv
f = open(args[1],'r')
sequense = ""
for line in f:
    if line[0] != '>':
        sequense += line.rstrip('\n')

gnum = sequense.count('g')
cnum = sequense.count('c')
##print(sequense)
print('gc含量:{}'.format((gnum+cnum)/len(sequense)))
f.close()