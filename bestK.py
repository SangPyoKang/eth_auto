import pyupbit
import numpy as np


def get_ror(k):
    df = pyupbit.get_ohlcv("KRW-ETH", count=4)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'],
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror

def get_best_k():
    rorList = list()
    kList = list()
    for k in np.arange(0.1, 0.99, 0.1):
        kList.append(k)
        rorList.append(get_ror(k))

    best_k_index =rorList.index(max(rorList))
    return kList[best_k_index]
    

