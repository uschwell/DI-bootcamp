import numpy as np
import pandas as pd

# lst = [2, 4, 6, 8, 13, 2020]
# numpy_arr = np.array(lst)
# print(numpy_arr)


# print(np.min(numpy_arr))
# print(np.mean(numpy_arr))
# print(np.product(numpy_arr))
# print(np.dot(numpy_arr,numpy_arr))
# print(np.subtract(numpy_arr, 4))



df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
# print(df)

df.info()
# df.head()