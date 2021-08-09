import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


to_read = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# data_Types=to_read.Series

# print(data_Types)

########continuous:PassengerId, Name, Age, ticket, fare, Cabin,
########categorical:Survived, Sex, Pclass,SibSp,Parch, Embarked
########Ordinal:Passenger-Id
########Nominal:Survived,Sex,

print(to_read)