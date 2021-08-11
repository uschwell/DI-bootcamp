import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# sns.catplot( "Sex", "Age", data=df, kind="box")
# plt.show()


train_df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
test_df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# combine = [train_df, test_df]

# print(train_df.columns.values)
# train_df.describe(include=['O'])


# train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)
# print(train_df.count("Survived"))
# train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)
# train_df[["Parch", "Survived"]].groupby(['Parch'], as_index=False).mean().sort_values(by='Survived', ascending=False)


# grid = sns.FacetGrid(train_df, row='Embarked', height=2.2, aspect=1.6)
# grid.map(sns.pointplot, 'Pclass', 'Survived', 'Sex', palette='deep')
# grid.add_legend()

#####Drop the Nan values (for plotting requirement)
train_df.dropna()
#####Plot how Age affected survival chances (separated by gender)
###As expected, extremely young, or extremely old passengers were in greater danger for survivng
sns.lineplot(x = "Age", y = "Survived",hue="Sex", data = train_df, estimator=(lambda x: len(x) / (2*len(df)) * 100))

# sns.displot(train_df, x="Age",y="Survived", kind="line")