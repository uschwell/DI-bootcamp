import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

to_read = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# data_Types=to_read.Series

# print(data_Types)

########continuous:PassengerId, Name, Age, ticket, fare, Cabin,
########categorical:Survived, Sex, Pclass,SibSp,Parch, Embarked
########Ordinal:Passenger-Id
########Nominal:Survived,Sex,

###We have 3 categories that we have discovered affected your survival changes.
to_read[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)
to_read[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)
to_read[["SibSp", "Survived"]].groupby(['SibSp'], as_index=False).mean().sort_values(by='Survived', ascending=False)




###lets plot out survival chance by age (separated by gender)
###As we can see below, 
# grid = sns.FacetGrid(to_read, col='Survived', row='Pclass', height=4.4, aspect=1.6)
# grid.map(plt.hist, 'Age', alpha=.5, bins=20)
# grid.add_legend();




###lets plot out survival chance by age (separated by gender)
# temp=to_read[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)
# temp2=to_read[["Age", "Survived"]].groupby(['Age'], as_index=False).mean().sort_values(by='Survived', ascending=False)
# temp2
# temp1
# grid = sns.FacetGrid(to_read, col='Survived', row='Sex', height=4.4, aspect=1.6)
# grid.map(plt.hist, 'Age', alpha=.5, bins=20)
# grid.add_legend()
# sns.lineplot(data=temp2, x="Age", y="Survived")


grid = sns.FacetGrid(to_read, row='Sex', height=4.4, aspect=1.6)
grid.map(sns.pointplot, 'Age', 'Survived', 'Sex', palette='deep')
grid.add_legend()

ax = sns.pointplot(x="Age", y="Survived", data=to_read, estimator=lambda x: len(x) / len(to_read) * 100)
ax.set(ylabel="Percent")