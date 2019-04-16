from sklearn import svm
from sklearn.datasets import load_svmlight_file
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt

X,y = load_svmlight_file('/Users/takei/Desktop/newcomer/MachineLearning/disorder.libsvm.dat')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)
lsvm = SVC(kernel='linear',C=1, probability=True)
lsvm.fit(X_train, y_train)
y_pred = lsvm.predict_proba(X_test)[:,1]

fpr, tpr, _ = metrics.roc_curve(y_test, y_pred)
auc = metrics.auc(fpr, tpr)
print(auc)
plt.plot(fpr, tpr)
plt.show()