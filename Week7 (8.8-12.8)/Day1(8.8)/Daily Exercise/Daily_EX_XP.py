import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ###############Step 1
# rand_arr=np.random.randint(low=0, high=75, size=(100,))
# print(rand_arr)





# ###############Step 2

# a = np.array([1,2,3,np.nan,5,6,7,np.nan])
# temp=np.isnan(a)
# a=(a[~np.isnan(a)])
# print(a)


# ###############Step 3
# new2d_array=np.random.randint(low=0, high=100, size=(5,6))
# print(new2d_array)


# ###############Step 4
# series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))


# df = pd.DataFrame(series)
# # print(df)
# temp=df.value_counts()
# # print(temp)

# in case we wanted to print or DISPLAY our results
# print(temp.plot.bar())
# temp.plot.bar()




# ###############Step 5
# series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
# # print(series)
# temp=pd.to_datetime(series)
# for i in temp:
#     print(i)
#     print("Year: "+str(i.year))
#     print("Month: "+str(i.month))
#     print("Day: "+str(i.day))


# ###############Step 6
to_read = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
to_read.head()
print(to_read)
# for col in to_read.columns:
#     print(col)


# ###############Step 7


# ###############Step 8


# ###############Step 9

# ###############Step 10

# ###############Step 11

# ###############Step 12

 # ###############Step 13