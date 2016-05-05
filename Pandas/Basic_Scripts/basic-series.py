'''
Some basic scripts/functions to manipulate data with pandas and a bit of numpy
'''

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from pandas_datareader import data,wb


"""
Basic code to setup and analyze a Pandas Series:
Series: One-dimensional array-like object containing an (Numpy) array of data and an array of labels, the index.
"""
def basicSeries():
    # Set just a series with numbers, the index is set automatically from 1 to len(Series)
    print ('-'*30, 'Series with Values','-'*30)
    series_1 = Series([1,2,3,4,5,6,10,4,6,0,12,23,12])
    print ('Series 1:\n{}'.format( series_1))
    print ('Index Series 1: \n{}'.format(series_1.index))
    print ('Values Series 1: \n{}'.format(series_1.values))
    print ('Get all values above 5: \n{}'.format(series_1[series_1 > 5]))


    # Set series with defined index
    print ('-'*30, 'Series with predefined Index','-'*30)
    series_2 = Series([1,2,3], index=['A','B','C'])
    print ('Index Series 2: \n{}'.format(series_2.index))
    print ('Values Series 2: \n{}'.format( series_2.values))
    print ('The value of index B is: \n{}'.format(series_2['B']))
    print ('Check if Index is in Series 2: \n{}'.format('E' in  series_2))


    # Create a Series from a Dictionary:
    print ('-'*30, 'Dict and Series','-'*30)
    dic = {'Bayern Munich': 1, 'Borussia Dortmund': 2, '1. FC Koeln': 3, 'HSV':4}
    series_dict = Series(dic)
    print ('Dict and Series: \n{}'.format(series_dict))


    # Series from values and index with NaN values:
    print ('-'*30, 'Series from values and index','-'*30)
    index = ['A', 'B', 'C', 'D']
    values = [1,2,3, None]
    series_3 = Series(values, index=index)
    print ('Series from values and index with NaN values: \n{}'.format(series_3))
    print ('Entries that are NaN: \n{}'.format(pd.isnull(series_3)))
    print ('Entries that are not NaN: \n{}'.format(pd.notnull(series_3)))
    series_3.index = ['E','F','G','H']
    print ('Change the index names: \n{}'.format(series_3))


def sortSeries():
    series_1 = Series([12,3,15,0,-143,23,None,89])
    print (series_1.order())
    print (series_1.sort_values)

def indexingSeries():
    series = Series(range(5), index = ['a','a','b','b','c'])
    print (series)
    print ('Duplicate index entries? \n{}'.format(series.index.is_unique))
    print (series['a'])


def uniqueValuesSeries():
    series = Series([1,2,3,3,3,4,5,6,7,8,7,6,7,8,9])
    print ('How much elements: \n{}'.format(series.count()))
    print ('How much unique elements: \n{}'.format(series.unique()))
    print (series.value_counts())


def hierachicalIndexingSeries():
    #Allows to have multiple (two or more) index levels on an axis. Provides a way for you to work with higher dimensional data in lower dimensional form
    series = Series(np.random.randn(10), index=[['a','a','a','b','b','b','c','c','d','d'],
                                                 [1,2,3,1,2,3,1,2,2,3]])
    print (series)
    print ('Take just the b part: \n{}'.format(series['b']))
    print ('Take the b and d part: \n{}'.format(series.ix[['b','d']]))
    print ('Inner level selection: \n{}'.format(series[:,2]))
    print ('Unstack the data: \n{}'.format(series.unstack()))
    print ('Make unstack to stack agaon: \n{}'.format(series.unstack().stack()))




if __name__ == '__main__':
    basicSeries()
    #sortSeries()
    #indexingSeries()
    #uniqueValuesSeries()
    #hierachicalIndexingSeries()
