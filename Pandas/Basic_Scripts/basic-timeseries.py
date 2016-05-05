import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from datetime import datetime
from dateutil.parser import parse
from matplotlib import pyplot




ts = Series(np.random.randn(24), index=pd.date_range('1/1/2000', periods=24, freq='M'))




def getActualTime():
    now = datetime.now()
    print ('Now: %s' %now)
    day = now.day
    month = now.month
    year = now.year
    print ('Today is the {} of {} of the year {}'.format(day,month,year))


def dateUtilTest():
    d1 = '2011-01-03'
    d2 = '2011/01/03'
    date1 = parse(d1)
    date2 = parse(d2)
    print ('Dateutil can parse different formats of dates b/c d1 {} is equal to d2 {}'.format(date1, date2))
    day = date2.day
    month = date2.month
    year = date2.year
    print ('The date is the {} of {} of the year {}'.format(day,month,year))


def tsBasic():
    dates = [datetime(2014,1,2), datetime(2014,1,3), datetime(2014,1,4), datetime(2014,1,5)]
    ts = Series(np.arange(4)+2, index=dates)
    print ('Representation of Time Series: \n%s' %  ts)


def shiftTs():
    dates = [datetime(2014,1,2), datetime(2014,1,3), datetime(2014,1,4), datetime(2014,1,5)]
    ts1 = Series(np.arange(4)+2, index=dates)
    #ts1 = ts1/ts1.shift(1) - 1
    print (ts1)
    ts1 = ts1.shift(1, freq='M')
    print (ts1)


def periodTs():
    rng = Series(np.random.randn(365),index= pd.date_range('1/1/2000', periods=365, freq='D'))
    print (rng.index)
    tsQ = rng.to_period(freq='Q-DEC')
    tsM = rng.to_period(freq='M')
    tsW = rng.to_period(freq='W')
    print (tsQ)
    print (tsM)
    print (tsW)


def resamplingFunction(x):
    return np.sum(x)*2


def returnFunction(x):
    N = len(x)-1
    x0 = x[0]
    xN = x[N]
    return (xN-x0)

def retFunction(x):
    N = len(x)-1
    x0 = x[0]
    xN = x[N]


def calcReturn():
    rng = Series(np.arange(13),index = pd.period_range('2010Q1','2011Q1', freq='M'))
    tsQ = rng.resample('Q-DEC', how=retFunction)




def resamplingTs():
    rng = Series(np.arange(13),index=pd.period_range('2010Q1','2011Q1',freq='M'))
    print (rng)
    tsQ1 = rng.resample('Q-DEC', how='mean')
    print (tsQ1)
    tsQ2 = rng.resample('Q-DEC', how=resamplingFunction)
    print (tsQ2)
    tsQ3 = rng.resample('Q-DEC', how=returnFunction)
    print (tsQ3)



def resamplingGroupBy():
    rng = Series(np.arange(13),index=pd.period_range('2010Q1','2011Q1',freq='M'))
    print (rng.index)
    tsQ1 = rng.groupby(lambda x: x.quarter).mean()
    print (tsQ1)


def movingWindow():
    pass



if __name__ == '__main__':
    #print (ts)
    #getActualTime()
    #dateUtilTest()
    #tsBasic()
    #shiftTs()
    periodTs()
    resamplingTs()
    resamplingGroupBy()