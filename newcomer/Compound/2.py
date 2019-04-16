from rdkit import Chem
from rdkit.Chem import MACCSkeys
from rdkit import DataStructs

m = Chem.MolFromSmiles("Cc1nc(Nc2ncc(s2)C(=O)Nc3c(C)cccc3Cl)cc(n1)N4CCN(CCO)CC4")
fps = MACCSkeys.GenMACCSKeys(m)
fp_bits = tuple(fps)
print(fp_bits)