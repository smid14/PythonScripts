'''
Script to analyze a DataSet of the cities of a specific country and the city population
'''

import pandas as pd
import numpy as np
import Quandl
import datetime
from matplotlib import pyplot as plt


def nBiggestCities(data, n):
    df = data.sort_values(by='Population')
    return df


def loadQuandlData():
    quandl_id = "hThEeCQhKC2oWz2hSB4x"
    it = Quandl.get(['GOOG/NASDAQ_AAPL','GOOG/NASDAQ_GOOGL','GOOG/NASDAQ_MSFT', 'GOOG/NASDAQ_FB','GOOG/NYSE_ORCL'], trim_start='1998-01-01', authtoken=quandl_id)
    financial = Quandl.get(['GOOG/NYSE_DB','GOOG/NYSE_GS','GOOG/NYSE_SAN'], authtoken=quandl_id)
    industrial = Quandl.get(['GOOG/NYSE_SI', 'GOOG/NYSE_GE'], authtoken=quandl_id)
    closing_it = it[['GOOG.NASDAQ_AAPL - Close','GOOG.NASDAQ_GOOGL - Close','GOOG.NASDAQ_MSFT - Close','GOOG.NASDAQ_FB - Close','GOOG.NYSE_ORCL - Close']]
    closing_financial = financial[['GOOG.NYSE_DB - Close','GOOG.NYSE_GS - Close','GOOG.NYSE_SAN - Close']]
    closing_industrial = industrial[['GOOG.NYSE_SI - Close','GOOG.NYSE_GE - Close']]
    closing_it.to_csv('Data/Closing_it.csv', sep=';')
    closing_financial.to_csv('Data/Closing_financial.csv', sep=';')
    closing_industrial.to_csv('Data/Closing_industrial.csv', sep=';')


def mergeDataFrames(it, financial, industrial):
    data = pd.concat([it, financial,industrial], join='inner', axis=1)
    stocks = ['Apple','Google','Microsoft','Facebook','Oracle','Deutsche Bank','Goldman Sachs', 'Santander', 'Siemens', 'General Electric']
    branches = ['IT', 'IT','IT','IT','IT','Financial','Financial','Financial','Industrial','Industrial']
    data.columns =[branches,stocks]
    data.reset_index(inplace=True)
    data.set_index(pd.DatetimeIndex(data['Date']), inplace=True)
    del data['Date']
    return data


def calculateDates(data):
    data.reset_index(inplace=True)
    data['YY'] = pd.Series(pd.DatetimeIndex(data['Date']).year)
    data['QQ'] = pd.Series(pd.DatetimeIndex(data['Date']).quarter)
    data['MM'] = pd.Series(pd.DatetimeIndex(data['Date']).month)
    data['WW'] = pd.Series(pd.DatetimeIndex(data['Date']).week)
    data['YY-MM'] = data['YY'].astype(str).str.cat(data['MM'].astype(str), sep='-')
    data['YY-WW'] = data['YY'].astype(str).str.cat(data['WW'].astype(str), sep='-W')
    data['YY-QQ'] = data['YY'].astype(str).str.cat(data['QQ'].astype(str), sep='-Q')
    del data['YY']
    del data['QQ']
    del data['MM']
    del data['WW']
    return data


def calculateReturn(data,freq):
    returns = data.pct_change()
    return_index = (1+returns).cumprod()
    if freq == 'quarter':
        returns = return_index.resample('Q-DEC', how='last').pct_change()
    elif freq == 'week':
        returns = return_index.resample('W', how='last').pct_change()
    elif freq == 'month':
        returns = return_index.resample('M', how='last').pct_change()
    return returns






if __name__ == '__main__':
   #loadQuandlData()
    it = pd.read_csv('Data/Closing_it.csv', sep=';', index_col = 0)
    financial = pd.read_csv('Data/Closing_financial.csv', sep=';', index_col = 0)
    industrial = pd.read_csv('Data/Closing_industrial.csv', sep=';', index_col = 0)
    data = mergeDataFrames(it,financial, industrial)
    #data = resampleData(data, 'week', 'mean')
    #print (data)
    returns = data.pct_change()
    returns = data.resample('Q-DEC')
    print (returns)
    ret_index = (1+returns).cumprod()
    print (ret_index)
    data['IT'].plot()
    returns['IT'].plot()
    ret_index['Industrial'].plot()
    plt.show()
