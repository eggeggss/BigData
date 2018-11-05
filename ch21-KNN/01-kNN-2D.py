#!/usr/bin/python
# -*- coding: utf-8 -*-
X = [[0,0], [1,0], [2,0], [3,0]]
y = [0, 0, 1, 1]
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y) 
#KNeighborsClassifier(...)
print("預測答案＝",neigh.predict([[1.1,0]]))
print("預測樣本距離＝",neigh.predict_proba([[1.1,0]]))   #      測試數據X的返回概率估計。