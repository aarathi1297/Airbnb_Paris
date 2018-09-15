# -*- coding: utf-8 -*-
"""
Airbnb Paris Data Munging: reads in the Airbnb geojson file, loads to Pandas dataframe for cleaning,
adding features for analysis, and handling missing values.


"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context("poster", font_scale=1.3)
import folium

import pandas as pd
import numpy as np
import json
import ijson
from datetime import datetime, timedelta

import os, sys
import warnings
warnings.filterwarnings('ignore')

import pivottablejs
import missingno as msno
import pandas_profiling

import ipywidgets as widgets

import sklearn
import scipy


mpl_update = {'font.size':16,
              'xtick.labelsize':14,
              'ytick.labelsize':14,
              'figure.figsize':[12.0,8.0],
              'axes.color_cycle':['#0055A7', '#2C3E4F', '#26C5ED', '#00cc66', '#D34100', '#FF9700','#091D32'], 
              'axes.labelsize':16,
              'axes.labelcolor':'#677385',
              'axes.titlesize':20,
              'lines.color':'#0055A7',
              'lines.linewidth':3,
              'text.color':'#677385'}
mpl.rcParams.update(mpl_update)



def get_arrond(row):
    ''' this function returns the arrondissement number based on the zipcode'''
    
    return int(row['zipcode'][-2:])

def get_arrond_name(row):
    '''this function returns the arrondissement name'''
    
    names = ['Louvre', 'Bourse', 'Temple', 'Hotel-de-Ville', 'Pantheon', 'Luxembourg',
             'Palais-Bourbon', 'Elysee', 'Opera', 'Entrepot', 'Popincourt', 'Reuilly','Gobelins',
             'Observaitoire', 'Vaugirard', 'Passy', 'Batignolles-Monceau',
             'Butte-Montmartre', 'Buttes-Chaumont', 'Menilmontant']
    return names[row['arrondissement'] - 1]

def set_rating_ind(row):
    '''this function checks the review_scores_rating and returns 0 if it is null (no rating),
       or 1 if a value is set'''
    if np.isnan(row['review_scores_rating']) == True:
        return 0
    else:
        return 1


#read and load the Airbnb Paris geojson file to a DataFrame
json_data_path = '../data/airbnb-listings.geojson.json'
with open(json_data_path, 'r') as f:
    objects = ijson.items(f, 'features.item')
    columns = list(objects)
    
#check that the expected number of rows have been read
print('number of rows read from json file: ',len(columns))

selected_row = []
for col in columns:
    temp = col['properties']
    selected_row.append(temp)

#load all rows to a dataframe
df = pd.DataFrame(selected_row)
pd.set_option('display.max_columns',500)

#Delete columns which will not be used for analysis
dfParis = df[['access','accommodates','amenities','availability_30','availability_60','availability_90','bathrooms','bedrooms','beds',
              'cancellation_policy','cleaning_fee','guests_included','host_since','host_total_listings_count',
              'id','last_review','latitude','longitude','minimum_nights','neighborhood_overview','neighbourhood_cleansed',
              'number_of_reviews','price','property_type','review_scores_accuracy','review_scores_checkin',
              'review_scores_cleanliness','review_scores_communication','review_scores_location',
              'review_scores_rating','review_scores_value','reviews_per_month','room_type','summary','transit','zipcode']
            ].copy()
    

#filter to only include properties in zip codes 75001 through 75021
zipcodes = [str(x) for x in range(75001, 75021) ]
dfParis = dfParis[dfParis['zipcode'].isin(zipcodes)]


#Add the following columns to be used for analysis   
#'arrondissement' and 'arrond_name': so we can refer to the area/location by arrondissement rather than the zipcode
dfParis['arrondissement'] = dfParis.apply(lambda x: get_arrond(x), 1)

dfParis['arrond_name'] = dfParis.apply(lambda x: get_arrond_name(x), 1)

#rating indicator 'rating_ind'.  Properties where scores_review_ratings is populated is set to 1, and 0 otherwise

dfParis['rating_ind'] = dfParis.apply(lambda x: set_rating_ind(x), 1)


#delete additional columns:
try:
    dfParis = dfParis.drop(['access','cleaning_fee','neighborhood_overview'], axis=1)
except:
    print('columns do not exist')
    
    
#delete the rows with missing values in the 'price' column, since they will not be useful in the analysis
delrows = dfParis[dfParis.price.isnull()]
dfParis = pd.merge(dfParis, delrows[['id']], how='outer', on='id', indicator=True)

try:
    dfParis = dfParis[dfParis['_merge']=='left_only']
    dfParis.drop('_merge', axis=1)
except:
    print('column does not exist')
    
print('last -- length of dfParis',len(dfParis))


#fill missing values for rows with null values in 'beds'
for i,row in dfParis.loc[dfParis['beds'].isnull(),:].iterrows():

    if np.isnan(dfParis.loc[i, 'bedrooms']) == False:
        dfParis.loc[i,'beds'] = dfParis.loc[i, 'bedrooms']
    else:
        dfParis.loc[i,'beds'] = 1
        dfParis.loc[i, 'bedrooms'] =1 

#fill missing values for rows with null values in 'bedrooms'
for i,row in dfParis.loc[dfParis['bedrooms'].isnull(),:].iterrows():

    if dfParis.loc[i, 'beds'] > 0 :
        dfParis.loc[i,'bedrooms'] = 1
    elif np.isnan(dfParis.loc[i, 'beds']) == True:
       #flats or studio type flats we can assume there is a bed, and count it as a bedroom
        dfParis.loc[i,'beds'] = 1
        dfParis.loc[i, 'bedrooms'] =1           
 
dfParis.to_pickle('../data/airbnb_Paris_cleansed_09015.p')

print('AirbnbParis_data_munging.py completed successfully')


