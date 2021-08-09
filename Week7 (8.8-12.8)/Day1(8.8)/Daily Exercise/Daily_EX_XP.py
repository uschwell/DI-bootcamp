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
# print(to_read)
# data_Types=to_read.dtypes
# print(data_Types)
#### print(data_Types.keys)
### item_counts = ["col1"].value_counts()
### print(item_counts)

# ###############Step 7
# to_read.drop("EngineSize", axis=1, inplace=True)
# del to_read['Length']

# ####check if EngineSize still exists
# if not "EngineSize" in to_read:
#     print("EngineSize has been removed")
# #####check if EngineSize still exists
# if not "Length" in to_read:
#     print("Length has been removed")

# ###############Step 8
# df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
#                     'weight': ['high', 'medium', 'low'] * 3,
#                     'price': np.random.randint(0, 15, 9)})

# df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
#                     'kilo': ['high', 'low'] * 3,
#                     'price': np.random.randint(0, 15, 6)})

# ###### new_df = pd.merge(df1, df2,  how='cross', left_on=True, right_on =True)
# #Merge the DataFrames
# df_merged = pd.merge(df1, df2, how='inner', left_index=True, right_index=True, suffixes=('', '_drop'))

# #Drop the duplicate columns
# df_merged.drop([col for col in df_merged.columns if 'drop' in col], axis=1, inplace=True)
# print('---------------------------------------')
# print(df1)
# print('---------------------------------------')
# print(df2)
# print('---------------------------------------')
# print(df_merged)
# print('---------------------------------------')



# ###############Step 9

df = pd.DataFrame(["STD,City\tState",
"33,Kolkata\tWest Bengal",
"44,Chennai\tTamil Nadu",
"40,Hyderabad\tTelengana",
"80,Bangalore\tKarnataka"], columns=['row'])

# Desired Output:
# 0 STD        City        State
# 1  33     Kolkata  West Bengal
# 2  44     Chennai   Tamil Nadu
# 3  40   Hyderabad    Telengana
# 4  80   Bangalore    Karnataka
df2 = pd.DataFrame(df.row.str.split(' ',1).tolist(),columns = ['STD','City','State'])

print(df2)
# ###############Step 10

# ###############Step 11

# ###############Step 12

 # ###############Step 13