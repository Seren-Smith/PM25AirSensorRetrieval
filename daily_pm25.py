# Import necessary packages
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from glob import glob

# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Use white grid plot background from seaborn
sns.set(font_scale=1.5, style="whitegrid")

file_path = 'C:/Users/Seren Smith/Documents/George Mason University/STC_Work/Purple Air/Pre-Processing/cal_LA_12_2021_matrix.csv'
coors = pd.read_csv('C:/Users/Seren Smith/Documents/George Mason University/STC_Work/Purple Air/Pre-Processing/cal_LA_12_2021_lat_long.csv')
# Import data using datetime and no data value
air_quality = pd.read_csv(file_path,
                                      parse_dates=['datetime'],
                                      index_col=['datetime'])

#air_quality = air_quality[['489', '2352', '5574', '6178', '22317', '23945', '31533', '37196']]
# idxport = np.where(air_quality[0] = coors[,0])
#air_quality = air_quality[['489', '2352', '5574', '23945', '24021', '27101', '28529', '31533', '37193', '56047', '57515', '57519', '86559']]

air_quality_daily = air_quality.resample('D').mean() # Daily Average
air_quality_daily = air_quality_daily[:-1]
air_quality_monthly = air_quality.resample('M').mean() # Monthly Average

air_quality_daily.to_csv('C:/Users/Seren Smith/Documents/George Mason University/STC_Work/Purple Air/Pre-Processing/cal_LA_12_2021_daily.csv')

air_quality_monthly.to_csv('C:/Users/Seren Smith/Documents/George Mason University/STC_Work/Purple Air/Pre-Processing/cal_LA_12_2021_monthly.csv')
