import pandas as pd
import glob
import os
import ast

pd.set_option("display.max_colwidth", None)
my_csv1 = pd.read_csv(r"federato_retention_csv1.csv")
df1 = pd.DataFrame(my_csv1)
my_csv2 = pd.read_csv(r"federato_retention_csv2.csv")
df2 = pd.DataFrame(my_csv2)
my_csv3 = pd.read_csv(r"federato_retention_csv3.csv")
df3 = pd.DataFrame(my_csv3)
# print(df.shape)
# df_copy = df.copy()

# print(df_copy.shape)

# print(df_copy['device_id'].nunique())
# print(df_copy['user_id'].unique())


print("Users who spent 10mins - 24hrs on the federato website")
print(df1.shape)
print(df1['event_type'].value_counts().head(20))
print()
print("Users who spent 0-60 sec on the federato website")
print(df2.shape)
print(df2['event_type'].value_counts().head(20))
print()
print("Users who spent 1-10 mins on the federato website")
print(df3.shape)
print(df3['event_type'].value_counts().head(20))