from zipfile import ZipFile
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import glob

d = {'col1': [1, 2]}
bigdataframe = pd.DataFrame(data=d)

extension = 'kmz'
folder = 'kmzfiles'
all_filenames = [i for i in glob.glob(f'{folder}/*.{extension}')]

for filename in all_filenames:
    kmz = ZipFile(filename, 'r')
    kml = kmz.open('doc.kml', 'r').read()

    soup = BeautifulSoup(kml, 'lxml')
    nameofbrigade = list(soup.find('name'))

    address=[]
    for i, html in enumerate(soup.find_all('address')):
        print(i, html.text)

        address.append(html.text)

    df = DataFrame (address, columns=[f'{nameofbrigade}'])
    df[f'{nameofbrigade}'] = df.apply(lambda x: x.str.split(' ').str[-2:].str.join(' '))
    bigdataframe = pd.concat([bigdataframe, df], axis=1)

bigdataframe.to_csv('data.csv', index=False)