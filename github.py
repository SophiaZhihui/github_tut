# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:30:21 2023

@author: jrbrad
"""

import pandas as pd

# function to extract the county FIPS code from the id column
# this function is completed as an example
def geoid_parse_cty_fip(row):
    return row['id'][9:14]

# function to extract the tract code from the id column
def geoid_parse_cty_tract(row):
    return (row['id'][-5:])

# function to extract the county name from the 'Geographic Area Name' column
# This function is completed as an example
# This function is the most complex of the final three functions
#    The remaining functions do not require the .join() function
def county_name(row):
    return ' '.join(row['Geographic Area Name'].strip().split(',')[1].split(' ')[:-1])

# function to extract the state name from the 'Geographic Area Name' column
def state_name(row):
    return #complete this statement

# function to extract the tract number from the 'Geographic Area Name' column
def tract_num(row):
    return #complete this statement

''' Instantiate DataFrame '''
filepath = 'DECENNIALPL2020.P1_data_with_overlays_2021-11-05T143124_mod.csv'
df = pd.read_csv(filepath)

''' Create new columns 'in DataFrame '''
''' Remove comments below as the respective functions are completed '''
df['fips'] = df.apply(geoid_parse_cty_fip, axis=1)
df['tract_geoid'] = df.apply(geoid_parse_cty_tract, axis=1)
df['name_county'] =  df.apply(county_name, axis=1)
#df['name_state'] =  df.apply(state_name, axis=1)
#df['num_tract'] =  df.apply(tract_num, axis=1)