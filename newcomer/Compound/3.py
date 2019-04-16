from rdkit import Chem
from rdkit.Chem import MACCSkeys,Draw
from rdkit import DataStructs
import matplotlib.pyplot as plt
import numpy as np
import random

m = Chem.MolFromSmiles("Cc1nc(Nc2ncc(s2)C(=O)Nc3c(C)cccc3Cl)cc(n1)N4CCN(CCO)CC4")
fp = MACCSkeys.GenMACCSKeys(m)

suppl = Chem.SDMolSupplier('/Users/TAKEI/Desktop/Python/newcomer/compound/cmpdlib.sdf')
mols = [mol for mol in suppl if mol is not None]
maccs_fps = [MACCSkeys.GenMACCSKeys(mol) for mol in mols]
maccs = np.array(DataStructs.BulkTanimotoSimilarity(fp,maccs_fps))

# plt.hist(maccs)
# plt.show()

similarityA = np.where(maccs>=0.8)
similarityB = np.where((maccs>=0.49)&(maccs<=0.51))
if len(similarityA[0]) >= 5:
    Asample = np.random.choice(similarityA[0], 5, replace = False)
Draw.MolsToImage([mols[index] for index in Asample])
if len(similarityB[0]) >= 5:
    Bsample = np.random.choice(similarityB[0], 5, replace = False)
Draw.MolsToImage([mols[index] for index in Bsample])