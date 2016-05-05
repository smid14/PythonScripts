
import pandas as pd
import numpy as np
from pandas import Series, DataFrame




def basicDataFrame():
    pass


def sortDataFrame():
    df = DataFrame({'a':[1,2,34,1,545,56,2,6,5,7],'b':[5,2,15,12,4,612,26,6,5,2], 'c':[2,3,4,0,34,12,4,64,1,3]})
    print (df)
    print (df.sort_values(by='c'))
    print (df.sort_index(by=['a','c']))



def applyDataFrame():
    df = DataFrame(np.arange(12).reshape(4,3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    print (df)
    f = lambda x: x.max() - x.min()
    func1 =  df.apply(f, axis = 0)
    func2 = df.apply(f, axis = 1)
    print (func1)
    print (func2)

    f2 = lambda x: '%.2f' % x
    df.applymap(f2)
    print (df.applymap(f2))


def indexingDataFrame():
    df = DataFrame(np.random.randn(4,3), index = ['a','a','b','b'])
    print (df)
    print ('Entries with index b: \n{}'.format(df.ix['b']))


def descriptiveStatsDataFrame():
    df = DataFrame([[1.4, np.nan], [7, 5], [np.nan, np.nan], [7,10]], index=['a','b','c','d'], columns=['one','two'])
    print (df)
    print ('Column Sum: \n{}'.format(df.sum(axis=0)))
    print ('Row Sum: \n{}'.format(df.sum(axis=1)))
    print ('Do not skip NA: \n{}'.format(df.sum(axis=1, skipna=False)))
    print ('Index with min Value: \n{}'.format(df.idxmin()))
    print ('Summary Statistic: \n{}'.format(df.describe()))


def correlationCovarianceDataFrame():
    all_data = {}
    for ticker in  ['AAPL','IBM','MSFT','GOOG']:
        all_data[ticker] = wb.download(ticker)
    price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.items()})
    volume = DataFrame({tic: data['Volume'] for tic, data in all_data.items()})
    print ('Price: \n{}'.format(price))


def uniqueValuesDataFrame():
    df = DataFrame({
        'Q1': [1,3,4,2,4],
        'Q2': [2,3,1,2,3],
        'Q3': [1,5,2,4,4]
    })
    print (df)
    res = df.apply(pd.value_counts)
    print ('How ofthe the values occur in the data: \n{}'.format(res))


def hierachicalIndexingDataFrame():
    #Allows to have multiple (two or more) index levels on an axis. Provides a way for you to work with higher dimensional data in lower dimensional form
    df = DataFrame(np.arange(12).reshape(4,3),
                   index=[['a','a','b','b'],[1,2,1,2]],
                   columns=[['Ohio','Ohio','Colorado'],
                            ['Green', 'Red','Green']])
    print (df)
    print (df['Ohio'])
    print (df.unstack())
    df.index.names = ['key1','key2']
    df.columns.names = ['state','color']
    print (df)
    print (df.swaplevel('key1','key2'))

def summaryStatDataFrame():
    df = DataFrame(np.arange(12).reshape(4,3),
                   index=[['a','a','b','b'],[1,2,1,2]],
                   columns=[['Ohio','Ohio','Colorado'],
                            ['Green', 'Red','Green']])
    df.index.names = ['key1','key2']
    df.columns.names = ['state','color']
    print (df)
    print ('Sum of key1: \n{}'.format(df.sum(level='key1')))
    print ('Sum of key2: \n{}'.format(df.sum(level='key2')))
    print ('Sum of state: \n{}'.format(df.sum(level='state', axis = 1)))
    print ('Sum of color: \n{}'.format(df.sum(level='color', axis = 1)))


def setIndexDataFrame():
    df = DataFrame({'a': range(7), 'b':range(7,0,-1),
                    'c':['one','one','one','two','two','two','two'],
                    'd':[0,1,2,0,1,2,3]})
    print (df)
    df2 = df.set_index(['c','d'])
    print (df2)
    df3 = df.set_index(['c','d'], drop=False)
    print (df3  )


if __name__ == '__main__':
    #applyDataFrame()
    sortDataFrame()
    #descriptiveStatsDataFrame()
    #correlationCovarianceDataFrame()
    #uniqueValuesDataFrame()
    #hierachicalIndexingDataFrame()
    #summaryStatDataFrame()
    #setIndexDataFrame()

