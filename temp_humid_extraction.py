import pandas as pd
import os, sys, glob

file_path = "../PM2.5Retrieval/11_LA_2021"

files = [f for f in os.listdir(file_path)]

def retrieve_temp_hum(files):
    dfs = []
    for file in files:
        print(file)
        df = pd.read_csv(file_path + '/' + file, encoding='latin-1', parse_dates=['data.datetime'], index_col=['data.datetime'])
        new = pd.DataFrame()
        #new['datetime'] = [df.iloc[0]['data.datetime']]
        new['datetime'] = [df.iloc[0]['data.datetime_A']]
        new['id'] = [df.iloc[0]['meta.ID']]
        new['temperature'] = [df.iloc[0]['data.temperature']]
        new['humidity'] = [df.iloc[0]['data.humidity']]

        new.to_csv(file_path + "/temp_hum/" + file)

#    concat_ids = pd.concat(dfs)
#    return concat_ids


temp_hum = retrieve_temp_hum(files)
#sample = pd.DataFrame(temp_hum)
temp_hum.datetime = pd.to_datetime(temp_hum.datetime)
temp_hum_hourly = temp_hum.resample('H', on = 'datetime').mean() # Hourly Average
#temp_hum_hourly = temp_hum_hourly.dropna()

# Currently aggregates everything?? needs to keep unique IDs
temp_hum_hourly.to_csv('C:/Users/Seren Smith/Documents/George Mason University/STC_Work/Purple Air/Pre-Processing/CA_QC_11_2021_temp_hum.csv', index=True)
