from rdkit import Chem
from rdkit.Chem import MACCSkeys,Draw,AllChem
from rdkit import DataStructs
import matplotlib.pyplot as plt
import numpy as np
import random

m = Chem.MolFromSmiles("Cc1nc(Nc2ncc(s2)C(=O)Nc3c(C)cccc3Cl)cc(n1)N4CCN(CCO)CC4")

fps = AllChem.GetMorganFingerprint(m, 2)
suppl = Chem.SDMolSupplier('compound/cmpdlib.sdf')
mols = [mol for mol in suppl if mol is not None]
ecfp4_fps = [AllChem.GetMorganFingerprint(mol, 2) for mol in mols]
ecfp4s = np.array(DataStructs.BulkTanimotoSimilarity(fps,ecfp4_fps))

plt.hist(ecfp4s)
plt.show()

# similarityA = np.where(ecfp4s>=0.8)
# similarityB = np.where((ecfp4s>=0.49)&(ecfp4s<=0.51))
# if len(similarityA[0]) >= 5:
#     Asample = np.random.choice(similarityA[0], 5, replace = False)
#     Draw.MolsToGridImage([mols[index] for index in Asample])
# if len(similarityB[0]) >= 5:
#     Bsample = np.random.choice(similarityB[0], 5, replace = False)
#     Draw.MolsToGridImage([mols[index] for index in Bsample])