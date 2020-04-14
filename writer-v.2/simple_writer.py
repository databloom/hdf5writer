#!/usr/bin/python


from pandas import (
    DataFrame, HDFStore
)
import pandas as pd
import numpy as np
import time


df = DataFrame(np.random.randn(100000,250000))

df.to_hdf('data-test-3.h5', key='df', mode='w')
#df.to_hdf('/gonzo/hdf5/'+timestr+'-data.h5',key='df', mode='w')

