import numpy as np


x= np.arrange(10).reshape(5,2)

y=['green', 'red', 'yellow',]


labeled={}
for i in range(len(y)):
    labeled[y[i]]=x[i]




class KNN:
    __init__(self, k_nearest):
        self.k_nearest=k_nearest


    def fit(X_train, Y_train):
        labeled={}
    for i in range(len(y)):
        labeled[y[i]]=x[i]

print("hello")





