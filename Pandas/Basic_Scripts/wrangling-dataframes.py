__author__ = 'manuel'


import pandas as pd
import numpy as np
from pandas import Series, DataFrame




def mergeDataframesInner():
    df1 = DataFrame({'key': ['c','c','b','b','a'], 'd1': range(5)})
    df2 = DataFrame({'key': ['d','c','b','c'], 'd2': range(4)})
    print ('DataFrame 1: \n{}'.format(df1))
    print ('DataFrame 2: \n{}'.format(df2))
    merged_df1_df2 = pd.merge(df1, df2)
    print ('Merge df1 on df2: \n{}'.format(merged_df1_df2))
    merged1_df1_df2 = pd.merge(df1, df2, on='key')
    print ('(Inner) Merge df1 on df2: \n{}'.format(merged1_df1_df2))


def mergeDataframesOuter():
    df1 = DataFrame({'lkey': ['c','c','b','b','a'], 'd1': range(5)})
    df2 = DataFrame({'rkey': ['d','c','b','c'], 'd2': range(4)})
    print ('DataFrame 1: \n{}'.format(df1))
    print ('DataFrame 2: \n{}'.format(df2))
    merged_df1_df2 = pd.merge(df1, df2, how='outer', left_on='lkey', right_on='rkey')
    print ('Outer Merge df1 on df2: \n{}'.format(merged_df1_df2))


def mergeDataframesLeft():
    df1 = DataFrame({'lkey': ['c','c','b','b','a'], 'd1': range(5)})
    df2 = DataFrame({'rkey': ['d','c','b','c'], 'd2': range(4)})
    print ('DataFrame 1: \n{}'.format(df1))
    print ('DataFrame 2: \n{}'.format(df2))
    merged_df1_df2 = pd.merge(df1, df2, how='left', left_on='lkey', right_on='rkey')
    print ('Left Merge df1 on df2: \n{}'.format(merged_df1_df2))


def mergeDataframesRight():
    df1 = DataFrame({'lkey': ['c','c','b','b','a'], 'd1': range(5)})
    df2 = DataFrame({'rkey': ['d','c','b','c'], 'd2': range(4)})
    print ('DataFrame 1: \n{}'.format(df1))
    print ('DataFrame 2: \n{}'.format(df2))
    merged_df1_df2 = pd.merge(df1, df2, how='right', left_on='lkey', right_on='rkey')
    print ('Right Merge df1 on df2: \n{}'.format(merged_df1_df2))

def multipleMerge():
    df1 = DataFrame({'key1': ['foo','foo','bar'],
                     'key2': ['one','two','one'],
                     'd1':   [1,2,3]})
    df2 = DataFrame({'key1': ['foo','foo','bar','bar'],
                     'key2': ['one','one','one','two'],
                     'd2': [4,5,6,7]})
    print ('DataFrame 1: \n{}'.format(df1))
    print ('DataFrame 2: \n{}'.format(df2))
    merged_df1_df2_multikeys = pd.merge(df1, df2, how='outer', on=['key1','key2'])
    print ('Outer Merge df1 on df2 with multiple  keys: \n{}'.format(merged_df1_df2_multikeys))
    merged_df1_df2 = pd.merge(df1, df2, on='key1', suffixes=['_left','_right'])
    print ('Inner Merge df1 on df2 with multiple keys: \n{}'.format(merged_df1_df2))


def indexMerge():
    left1 = DataFrame({'key': ['a','b','a','a','b','c'],
                       'value': range(6)})
    right1 = DataFrame({'group_val':[3.5, 7]}, index=['a','b'])
    print ('Data Frame 1: \n{}'.format(left1))
    print ('Data Frame 2: \n{}'.format(right1))
    merge_inner = pd.merge(left1, right1, left_on='key', right_index=True)
    print ('Merge on Key left and right on Index: \n{}'.format(merge_inner))
    merge_outer = pd.merge(left1, right1, left_on='key', right_index=True, how='outer')
    print ('Merge Outer on Key left and right on Index: \n{}'.format(merge_outer))


def hierarchicallyIndexMerge():
    lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                       'key2': [2000, 2001, 2002, 2001, 2002],
                       'data': np.arange(5.)})
    righth = DataFrame(np.arange(12).reshape((6, 2)),
                       index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                              [2001, 2000, 2000, 2000, 2001, 2002]],
                       columns=['event1', 'event2'])
    print ('DataFrame 1: \n{}'.format(lefth))
    print ('DataFrame 2: \n{}'.format(righth))
    merge_inner = pd.merge(lefth,righth,left_on=['key1','key2'], right_index=True)
    print ('Inner Merged DataFrame: \n{}'.format(merge_inner))
    merge_outer = pd.merge(lefth,righth,left_on=['key1','key2'], right_index=True, how='outer')
    print ('Outer Merged DataFrame: \n{}'.format(merge_outer))

    left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                      index=['a', 'c', 'e'],
                      columns=['Ohio', 'Nevada'])
    right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                       index=['b', 'c', 'd', 'e'],
                       columns=['Missouri','Alabama'])
    print ('Data Frame 1: ', left2)
    print ('Data Frame 2: ', right2)
    merge = pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
    print ('Merge: \n{}'.format(merge))



if __name__ == "__main__":
    hierarchicallyIndexMerge()