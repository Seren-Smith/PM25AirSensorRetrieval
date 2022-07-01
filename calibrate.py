import os, sys, glob
import pandas as pd

file_path = 'C:/Users/Seren Smith/Documents/George Mason University/STC_Work/Purple Air/Pre-Processing/PurpleAirData/LA_12_2021'

files = [f for f in os.listdir(file_path)]

for file in files:
    print(file)
    df2 = pd.read_csv(file_path + '/' + file, encoding='latin-1')
    a0 = 6.0589
    a1 = 0.61371
    a2 = -0.0007
    a3 = -0.0234
    a4 = -0.0419
    calibrate = (a0 + (a1 * df2['data.pm25_A']) + (a2 * (df2['data.pm25_A'] * df2['data.pm25_A'])) + (a3 * df2['data.temperature']) + (a4 * df2['data.humidity']))
    df2['calibrated'] = calibrate

    df2.to_csv(file_path + "/" + file)
