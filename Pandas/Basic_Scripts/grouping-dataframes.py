import pandas as pd
import numpy as np
from pandas import Series, DataFrame


df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                    'key2' : ['one', 'two', 'one', 'two', 'one'],
                    'data1' : np.random.randn(5),
                    'data2' : np.random.randn(5)})




def firstGrouping():
    print ("Data Frame: \n{}".format(df))
    grouped_1 = df['data1'].groupby(df['key1']) # = df.groupby('key1')['data1']
    print ("Grouped mean of data1 column based on key1: \n{}".format(grouped_1.mean()))
    grouped_2 =df['data1'].groupby([df['key1'],df['key2']])
    print ("Grouped mean of data1 column based on key1 and key2: \n{}".format(grouped_2.mean()))
    grouped_3 =df['data1'].groupby([df['key2'],df['key1']])
    print ("Grouped mean of data1 column based on key2 and key1: \n{}".format(grouped_3.mean()))
    print ("Unstack the result of 3: \n{}".format(grouped_3.mean().unstack()))
    states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
    years = np.array([2005,2005,2006,2005,2006])
    grouped_4 = df['data1'].groupby([states,years]).mean()
    print ("New split keys: \n{}".format(grouped_4))
    grouped_5 = df.groupby('key1').mean()
    grouped_6 = df.groupby(['key1','key2'])
    print ("Both datasets are split by key1: \n{}".format(grouped_5))
    print ("Both datasets are split by key1 and key2: \n{}".format(grouped_6.mean()))
    print ("Get size of the groups: \n{}".format(grouped_6.size()))


def iteratingGroups():
    for name,group in df.groupby('key1'):
        print ('Key name: %s' % name)
        print ('Group data: %s' % group)


    for (k1,k2), group in df.groupby(['key1','key2']):
        print ((k1,k2))
        print ('Group data: %s' % group)


def dictGroups():
    pieces = dict(list(df.groupby('key1')))
    print ("Dict of the grouped data by key1: \n")
    for key in pieces:
        #print ("Key 1: %s" % key)
        #print ("Data: \n %s" % data)
        print (key)
        for e in key:
            print (e)

def groupbyAxis1():
    grouped = df.groupby(df.dtypes, axis=1)
    print (dict(list(grouped)))


def groupWithDicts():
    people = DataFrame(np.random.randn(5,5),
                       columns=['a','b','c','d','e'],
                       index = ['Anne', 'Manuel', 'Julia', 'Klaus', 'Hans'])
    maps = {'a':'red','b':'green', 'c':'blue','d':'orange','e':'yellow'}
    group_by_col = people.groupby(maps, axis = 1)
    print (group_by_col.sum())
    print (group_by_col.count())
    maps = {'a':'red','b':'red', 'c':'blue','d':'orange','e':'yellow'}
    group_by_col = people.groupby(maps, axis = 1)
    print (group_by_col.sum())
    print (group_by_col.count())

    group_by_len = people.groupby(len)
    print (group_by_len.sum())
    print (group_by_len.count())



def groupWithIndexLevel():
    columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                         [1, 3, 5, 1, 3]], names=['cty', 'tenor'])
    hier_df = DataFrame(np.random.randn(4, 5), columns=columns)
    print (hier_df)
    grouped = hier_df.groupby(level = 'cty', axis=1).count()
    print (grouped)


def groupAggregation():
    pass



if __name__ == "__main__":
    #firstGrouping()
    #iteratingGroups()
    #dictGroups()
    #groupbyAxis1()
    #groupWithDicts()
    groupWithIndexLevel()