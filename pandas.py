# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:21:08 2019

@author: joshuaheyer
"""

## Change working directory 

os.chdir(" ")

##### Pandas tutorial ########################################

## "as" pd shortens the name since we will be using pandas a lot 
import pandas as pd

### Create a dataframe from scratch 

data = {
        'apples': [3, 2, 0, 1],
        'oranges': [0, 3, 7, 2]
}


## Pass dataframe to pandas DataFrame constructor: 

purchases = pd.DataFrame(data)

purchases


## Make customer names as our index

purchases = pd.DataFrame(data, index=['June','Robert','Lily','David'])

purchases


## Locate customer's order by using their name 

purchases.loc['June']


### Read in data from CSVs

df = pd.read_csv('pandas.csv')

df

## csv's do not need indexes like dataframes. Can designate the index_col when reading
## Setting index column to zero 

df = pd.read_csv('pandas.csv', index_col=0)

df

##  Other important DataFrame Operations 

teams_df = pd.read_csv('data2.csv', index_col="Team")

## head outputs first 5 rows of dataframe by default. Can do more rows
teams_df.head()
teams_df.head(10)

## Tails outputs last 5 rows by default 
teams_df.tail(2)


## info() good command to run when first opening data

teams_df.info()

## shape() outputs a tuple of rows, columns 

teams_df.shape


## Handling duplicates #####
## Use append() to return a copy without affecting original dataframe -- create duplicates for this example 

temp_df = teams_df.append(teams_df)
temp_df

## drop duplicates

temp_df = temp_df.drop_duplicates()

temp_df.shape

## keep argument 

temp_df = teams_df.append(teams_df)

## keep drops all duplicates. If two rows are the same they are both dropped 
temp_df.drop_duplicates(inplace=True, keep=False)

temp_df.shape
temp_df

## see column names 

teams_df.columns

## Rename column 
teams_df.rename(columns={
        'Town': 'Cities',
        }, inplace = True)



