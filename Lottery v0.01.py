
import pandas as pd
import numpy as np


import os
import sys



import io
import requests


pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)


df = pd.read_csv('https://www.national-lottery.co.uk/results/lotto/draw-history/csv')


df = df[['Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5', 'Ball 6',
       'Bonus Ball']]
df = df.apply(pd.value_counts).fillna(0).astype('int')
df['total'] = df.sum(axis=1).astype('int')

df.insert(0, 'Number', range(1, 1 + len(df)))
df

df.to_excel('lottery_count.xlsx', index=False)
df.total.hist(bins=10);



df = pd.read_csv('https://www.national-lottery.co.uk/results/euromillions/draw-history/csv')


df = df[['Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5',
       'Lucky Star 1', 'Lucky Star 2']]
df = df.apply(pd.value_counts).fillna(0).astype('int')
df['total'] = df.sum(axis=1).astype('int')

df.insert(0, 'Number', range(1, 1 + len(df)))
df

df.to_excel('euro_lottery_count.xlsx', index=False)
df.total.hist(bins=10);

