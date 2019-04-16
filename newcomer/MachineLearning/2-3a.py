from sklearn.datasets import load_svmlight_file
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics


param_grid = {'C':[0.001,0.01,0.1,1,10,100]}
X,y = load_svmlight_file('MachineLearning/disorder.libsvm.dat')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)
grid_search = GridSearchCV(SVC(kernel = 'linear'), param_grid, scoring= 'roc_auc')
grid_search.fit(X_train, y_train)
best_c = grid_search.best_params_
print(best_c)
print('best_auc: {}'.format(metrics.roc_auc_score(y_test, grid_search.decision_function(X_test))))