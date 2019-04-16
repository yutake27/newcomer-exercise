from sklearn import svm
from sklearn.datasets import load_svmlight_file
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt

cost_param = [0.001, 0.01, 0.1, 1, 10, 100]
best_auc = 0
best_cost_param = 0
X,y = load_svmlight_file('MachineLearning/disorder.libsvm.dat')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)
for c in cost_param:
    lsvm = SVC(kernel = 'linear', C = c, probability = True)
    lsvm.fit(X_train, y_train)
    y_pred = lsvm.predict_proba(X_test)[:,1]
    fpr, tpr, _ = metrics.roc_curve(y_test, y_pred)
    auc = metrics.auc(fpr, tpr)
    if auc > best_auc:
        best_auc = auc
        best_cost_param = c
print("best C: {},best auc: {}".format(best_cost_param,best_auc))