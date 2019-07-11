#From: https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html
import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

print(X)

Y = np.array([1, 1, 1, 2, 2, 2])

print(Y)

clf = GaussianNB()

# Pode usar fit ou partial_fit
clf.fit(X, Y)

print("predict",clf.predict([[-0.8, -1]]))

clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))

print("pos- partial_fit", clf_pf.predict([[-0.8, -1]]))