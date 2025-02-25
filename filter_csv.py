import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import glob
import os




pd.set_option("display.max_colwidth", None)


csv1_folder = "1_csv"
csv2025_folder = "2025_csv"

csv1_files = glob.glob(os.path.join(csv1_folder, "*.csv"))
csv2025_files = glob.glob(os.path.join(csv2025_folder, "*.csv"))
files = csv1_files + csv2025_files
output_file = "federato_retention_csv2.csv"


# CHANGE THIS (retention_minutes)
retention_seconds = 25
daily_limit = 86400

# If running this code again, uncomment the two lines below
# if os.path.exists(output_file):
#     os.remove(output_file)


with open(output_file, 'w') as f:
    first_csv = True
    for file in files:
        
        for df in pd.read_csv(file,chunksize=100000):

            df_copy = df.copy()

            df_copy["client_event_time"] = pd.to_datetime(df_copy["client_event_time"])
            df_copy["Client_Start_Int"] = df_copy['client_event_time'].astype('int64')//10**9
            df_copy["client_upload_time"] = pd.to_datetime(df_copy["client_upload_time"])
            df_copy["Client_End_Int"] = df_copy['client_upload_time'].astype('int64')//10**9

            df_copy["Client_Time_Spent"] = df_copy["Client_End_Int"] - df_copy["Client_Start_Int"]
            
            df_filtered = df_copy[(df_copy["Client_Time_Spent"] > 0) & (df_copy["Client_Time_Spent"] < 60)]
            df_filtered.to_csv(output_file,header=first_csv,index=True,mode='a')
            first_csv = False
            