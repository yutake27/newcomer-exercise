import sys
import numpy as np

args = sys.argv
filename = args[1]
chain = args[2]
# chain = 'A'
# f = open('Protein/1buw.pdb')
f = open(filename)

x = []
y = []
z = []
for line in f:
    if line[0:4] == 'ATOM':
        if line[12:16].find('CA'):
            if line[21] == chain:
                x.append(float(line[30:38]))
                y.append(float(line[38:46]))
                z.append(float(line[46:54]))
x = x - np.mean(x)
y = y - np.mean(y)
z = z - np.mean(z)

distance = np.sqrt(x**2 + y**2 + z**2)
r = np.mean(distance)
print('radius: {}'.format(r))

