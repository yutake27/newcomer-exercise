import sys
import numpy as np

args = sys.argv
if len(args) != 3:
    print("argument error")
    quit()
filename = args[1]
chain = args[2]
f = open(filename)

x = []
y = []
z = []
id = []
for line in f:
    if line[0:4] == 'ATOM':
        if line[12:16].find('CA'):
            if line[21] == chain:
                id.append(int(line[6:11]))
                x.append(float(line[30:38]))
                y.append(float(line[38:46]))
                z.append(float(line[46:54]))
x = x - np.mean(x)
y = y - np.mean(y)
z = z - np.mean(z)

distance = np.sqrt(x**2 + y**2 + z**2)
r = np.mean(distance)
in_atoms = []
out_atoms = []
for i in range(len(distance)):
    if distance[i] <= r:
        in_atoms.append(id[i])
    else:
        out_atoms.append(id[i])
str_in_atoms = ','.join(map(str,in_atoms))
str_out_atoms = ','.join(map(str,out_atoms))

f_out = open('Protein/script.py', 'w')
f_out.write('pymol.cmd.load(\'{}\')\n'.format(filename))
f_out.write('pymol.cmd.do(\'hide everything\')\n')
f_out.write('pymol.cmd.do(\'sel inter,(id {})\')\n'.format(str_in_atoms))
f_out.write('pymol.cmd.do(\'sel exter,(id {})\')\n'.format(str_out_atoms))
f_out.write('pymol.cmd.do(\'show cartoon, inter\')\n')
f_out.write('pymol.cmd.do(\'show cartoon, exter\')\n')
f_out.write('pymol.cmd.do(\'color red, inter\')\n')
f_out.write('pymol.cmd.do(\'color blue, exter\')\n')
f_out.write('pymol.cmd.do(\'png Protein/3chain{}.png\')'.format(chain))
f_out.close()

# import pymol

# pymol.finish_launching()
# pymol.cmd.load(filename)
# pymol.cmd.do('hide everything')
# pymol.cmd.do('sel inter,(id {})'.format(str_in_atoms))
# pymol.cmd.do('sel exter,(id {})'.format(str_out_atoms))
# pymol.cmd.do('show cartoon, inter')
# pymol.cmd.do('show cartoon, exter')
# pymol.cmd.do('color red, inter')
# pymol.cmd.do('color blue, exter')
# pymol.cmd.do('png Protein/3.png')
# pymol.cmd.refresh()
# pymol.cmd.quit()