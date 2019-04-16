import sys
import numpy as np
import matplotlib.pyplot as plt

args = sys.argv
if len(args) != 4:
    print('Error')
    quit()
f = open(args[1],'r')
window =  int(args[2])
step = int(args[3])
sequense = ""
for line in f:
    if line[0] != '>':
        sequense += line.rstrip('\n')

gnum = sequense.count('G')
cnum = sequense.count('C')
##print(sequense)
print('gc含量:{}'.format((gnum+cnum)/len(sequense)))
i = 0
gc = []
position = []
while i < len(sequense):
    gnum = sequense[i:i+window].count('G')
    cnum = sequense[i:i+window].count('C')
    gc.append((gnum+cnum)/window)
    print((gnum+cnum)/window)
    position.append(i)
    i += step

left = np.array(position)
height = np.array(gc)
plt.plot(left,height)
plt.show()
f.close()