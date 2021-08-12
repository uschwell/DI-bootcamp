import numpy as np
import pandas as pd
import sklearn
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split

# x= np.arrange(10).reshape(5,2)

# y=['green', 'red', 'yellow',]


# labeled={}
# for i in range(len(y)):
#     labeled[y[i]]=x[i]




class KNN:
    def __init__(self, n):
        self.n=n


    def fit(self, X_train, Y_train):
        self.X_train= X_train
        self.Y_train= Y_train

    def predict(self, X_test):
        y_guess = []
        for test in X_test:
            distances=[]
            for rows in X_test:
                dist = np.linalg.norm(test - rows)
                distances.append(dist)
            indices = list(np.argpartition(distances, self.n)[:self.n])
            ind_lables= self.Y_train.iloc[indices]
            count=ind_lables.value_counts()
            max_val=count.idxmax()
            y_guess.append(max_val)




