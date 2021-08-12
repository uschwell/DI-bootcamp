
import sklearn
import statistics
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np





def findIQR(self, all, Q1in, Q3in):
    Q1=statistics.median(Q1in)
    Q3=statistics.median(Q3in)
    IQR=(Q3-Q1)

    return IQR



boston=load_boston()
boston_df=pd.DataFrame(boston.data,columns=boston.feature_names)
boston_df['Price']=boston.target


price_List=boston.target
# print(price_List)


#we find the median
priceMed=statistics.median(price_List)
# print(priceMed)
# print(type(priceMed))
# print(type(price_List))

Q1arr=[]
Q3arr=[]

for price in price_List:
    if(price<=priceMed):
        Q1arr.append(price)
    else:
        Q3arr.append(price)

# print(Q1)
# print(Q3)