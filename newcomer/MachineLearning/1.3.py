import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from collections import Counter

iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size = 0.33)

K = [1, 5, 10]
for k in K:
    y_pred = []
    for x_test in X_test:
        distances = np.array([np.sum((x_test - x_train)**2) for x_train in X_train])
        nearest_indexes = distances.argsort()[:k]
        nearest_labels = y_train[nearest_indexes]
        c = Counter(nearest_labels)
        y_pred.append(c.most_common()[0][0])
    print("k = {}, accuracy = {}".format(k,np.mean(y_pred == y_test)))
