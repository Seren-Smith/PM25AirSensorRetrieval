import os, sys, glob
from os import listdir
from os.path import isfile, join
import pandas as pd

file = "../PM2.5Retrieval/SB_10_12_2021/meta.csv"

df = pd.read_csv(file, encoding='latin-1')

new = pd.DataFrame()
new['id'] = df['ID']
new['lat'] = df['latitude']
new['lon'] = df['longitude']

purple_air_lat_long = new

purple_air_lat_long.to_csv('C:/Users/Seren Smith/Documents/George Mason University/STC_Work/Purple Air/Pre-Processing/SB_10_12_2021_lat_long.csv', index=False)
