from sklearn import svm
from sklearn.datasets import load_svmlight_file
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
import numpy as np

X,y = load_svmlight_file('MachineLearning/disorder.libsvm.dat')
lsvm = LinearSVC()
scores = cross_val_score(lsvm, X, y, cv = 5)
print(np.mean(scores))