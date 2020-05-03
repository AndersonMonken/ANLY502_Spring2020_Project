#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:09:55 2020

@author: anderson
"""
import requests
import os
from multiprocessing import Pool
import tarfile
import gzip
import shutil
import io

num_threads = 18

#Downloading data for 502 project

raw_telescope_files = [{'telescopetype' : 'F10', 'years' : [1992,1994]},
{'telescopetype' : 'F12', 'years' : [1994,1999]},
{'telescopetype' : 'F14', 'years' : [1997,2003]},
{'telescopetype' : 'F15', 'years' : [2000,2007]},
{'telescopetype' : 'F16', 'years' : [2004,2009]},
{'telescopetype' : 'F18', 'years' : [2010,2013]}]

url_file_list = []

for raw_file_type in raw_telescope_files:
    for year_i in range(raw_file_type['years'][0],raw_file_type['years'][1]+1):
        url_file_list.append([raw_file_type['telescopetype'],year_i])


def tar_download(info_list):
    url = str('https://ngdc.noaa.gov/eog/data/web_data/v4composites/' + 
                             info_list[0] + str(info_list[1]) + '.v4.tar')
    folder_path = f'/home/anderson/Downloads/nightlight/raw/{info_list[0]}{info_list[1]}'
    folder_out_path = f'/home/anderson/Downloads/nightlight/output/{info_list[0]}{info_list[1]}'
    
    file_path = os.path.join(folder_path,f'{info_list[0]}{info_list[1]}.tar')
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    if not os.path.exists(folder_out_path):
        os.mkdir(folder_out_path)
    #myfile = requests.get(url)
    #open(file_path, 'wb').write(myfile.content)
    try:
        with tarfile.open(file_path) as tf:
            tf.extractall(folder_out_path)
    except:
        print(file_path + ' failed to open')
    
with Pool(num_threads) as pool:
    results = pool.map(tar_download, url_file_list)

def ungzfiles(info_list):
    folder_path = f'/home/anderson/Downloads/nightlight/output/{info_list[0]}{info_list[1]}'
    folder_out_path = f'/home/anderson/Downloads/nightlight/output/{info_list[0]}{info_list[1]}'
    if not os.path.exists(folder_out_path):
        os.mkdir(folder_out_path)
    for r, d, f in os.walk(folder_path):
        for file_i in f:
            if file_i[-3:] == '.gz':
                fpath_in = os.path.join(folder_path, file_i)
                fpath_out = os.path.join(folder_out_path, file_i.replace('.gz',''))
                shutil.copyfileobj(gzip.GzipFile(fpath_in), open(fpath_out, 'wb'))
                os.remove(fpath_in)

with Pool(num_threads) as pool:
    results = pool.map(ungzfiles, url_file_list)
