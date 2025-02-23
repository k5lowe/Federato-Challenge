import pandas as pd
from datetime import datetime



csv1 = r"1_csv\amplitude_export_chunk_1_anonymized_subchunk_0_100000.csv"

first_file1 = pd.read_csv(csv1)
df = pd.DataFrame(first_file1)

print(df.shape)

# print(df.columns)
# df.drop(['$insert_id', ])
# print(df[['client_event_time','client_upload_time']])

df_copy = df.copy()

# print(df_copy[['client_event_time','client_upload_time']])


df_copy["client_event_time"] = pd.to_datetime(df_copy["client_event_time"])
df_copy["Client_Start_Int"] = df_copy['client_event_time'].astype('int64')//10**9

df_copy["client_upload_time"] = pd.to_datetime(df_copy["client_upload_time"])
df_copy["Client_End_Int"] = df_copy['client_upload_time'].astype('int64')//10**9

df_copy["Time_Spent"] = df_copy["Client_End_Int"] - df_copy["Client_Start_Int"]


# print((df_copy[["client_event_time","client_upload_time"]]).head(40))
# print(df_copy[['client_event_time','Client_Start_Int']])
# print((df_copy[['Client_Start_Int','Client_End_Int', 'Time_Spent']]).head(40))
# print(len(df_copy.columns))
# df_copy = df_copy.drop(['$insert_id','client_event_time','client_upload_time'])
df_copy = df_copy.drop(columns=['$insert_id', 'client_event_time', 'client_upload_time'])

print(df_copy.columns)

# print(df_copy[['Client_Start_Int','Client_End_Int', 'Time_Spent']])