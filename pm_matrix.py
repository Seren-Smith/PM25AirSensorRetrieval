import pandas as pd
import os
from tqdm import tqdm
from glob import glob
import datetime
import numpy as np

def get_matrix(target_df, station_df, source_files, attr):
    """
    :param t_range: predefined time range df
    :param station_df: selected stations
    :param source_files: all data by stations
    :param attr:
    :return:
    """
    target_df = target_df.set_index('datetime')

    for sid in tqdm(source_files):
        try:
            s_df = pd.read_csv(sid,
                               usecols=['data.datetime', attr],
                               index_col=['data.datetime'])
            s_df[attr].values[s_df[attr] > 150] = 150
            name = {}

            base = os.path.basename(sid)
            sid = os.path.splitext(base)[0].split('_')[1]
            name[sid] = sid
            s_df = s_df.rename(columns= {attr: name[sid]})

            s_df.index = pd.to_datetime(s_df.index)
            target_df = target_df.join(s_df)
        except:
            print(f'skip {sid}')

    return target_df

# predefined time range
start = datetime.date(2021, 11, 1)
end = datetime.date(2021, 12, 1)
rng = pd.DataFrame()
rng['datetime'] = pd.date_range(start=start, end=end, freq='1min')

data_path = 'C:/Users/Seren Smith/Documents/George Mason University/STC_Work/Purple Air/Pre-Processing/PurpleAirData/cal_QC_11_2021'
files = glob(data_path + r'\*.csv')

coors = pd.read_csv('C:/Users/Seren Smith/Documents/George Mason University/STC_Work/Purple Air/Pre-Processing/cal_QC_11_2021_lat_long.csv', index_col=['id'])
#updated_matrix = get_matrix(rng, coors, files, 'data.pm25_A')
updated_matrix = get_matrix(rng, coors, files, 'calibrated')

updated_matrix.to_csv('C:/Users/Seren Smith/Documents/George Mason University/STC_Work/Purple Air/Pre-Processing/cal_QC_11_2021_matrix.csv')
