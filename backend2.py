import pandas as pd
import glob
import os
import ast

pd.set_option("display.max_colwidth", None)
my_csv = pd.read_csv(r"federato_retention_csv2.csv")
df = pd.DataFrame(my_csv)

print(df.shape)
# df_copy = df.copy()

# print(df_copy.shape)

# print(df_copy['amplitude_id'].nunique())
# print(df_copy['device_id'].nunique())
# print(df_copy['user_id'].nunique())








# df_filtered = df_copy[(df_copy["Client_Time_Spent"] > 0) & (df_copy["Client_Time_Spent"] < 40)]["Client_Time_Spent"]
# print(df_filtered.shape)
# plt.hist(df_filtered, bins=20, edgecolor='black', alpha=0.7)
# plt.show()

# lis = ['$insert_id', 'amplitude_id', 'app', 'city', 'client_event_time',
#     'client_upload_time', 'country', 'data', 'data_type', 'device_family',
#     'device_id', 'device_type', 'dma', 'event_id', 'event_properties',
#     'event_time', 'event_type', 'language', 'library', 'os_name',
#     'os_version', 'platform', 'processed_time', 'region',
#     'server_received_time', 'server_upload_time', 'session_id', 'user_id',
#     'user_properties', 'uuid', 'Client_Start_Int', 'Client_End_Int',
#     'Server_Start_Int', 'Server_End_Int', 'Client_Time_Spent',
#     'Server_Time_Spent']


# app, data_type, platform (web) have one value

# print(df_filtered[key])
# print(df_filtered[key].nunique())

# print(df_copy['Client_Time_Spent'].value_counts())


# print(df_copy['city'].nunique())
# print(df_copy['country'].nunique())
# print(df_copy['data'].nunique())
# print(df_copy['device_family'].nunique())



# print(df_copy['city'].value_counts().head(10))
# print(df_copy['country'].value_counts())
# print(df_copy['data'].value_counts())
# print(df_copy['device_family'].value_counts())
# # print(df_copy['region'].value_counts())
# print(df_copy['platform'].value_counts())


# a = df_copy['user_properties'][0]
# print(type(a))
# dct = ast.literal_eval(a)


# print(dct.keys())
# print(dct.values())
# print(df_filtered['dma'].value_counts())
# print(df_copy['device_type'].value_counts())
# print(df_filtered['device_type'].value_counts())




# df_filtered['city'].value_counts().plot(kind="bar")
# plt.show()
