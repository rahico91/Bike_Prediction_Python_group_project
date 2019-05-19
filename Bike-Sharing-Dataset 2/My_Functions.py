import numpy as np
import pandas as pd
import seaborn as sns
import warnings

import dask
from dask.distributed import Client, progress
import dask.dataframe as dd
import dask.array as da
from dask import delayed
import graphviz

'''dask_ml.preprocessing contains some of the functions from sklearn like RobustScalar, StandardScalar, LabelEncoder, OneHotEncoder, PolynomialFeatures etc., and some of its own such as Categorizer, DummyEncoder, OrdinalEncoder etc'''

from dask_ml.preprocessing import Categorizer, DummyEncoder, MinMaxScaler
from dask_ml.datasets import make_regression
from dask_ml.model_selection import train_test_split#, GridSearchCV
from dask_ml.metrics import r2_score

from dask_ml.linear_model import LinearRegression
from dask_glm.datasets import make_regression


from sklearn.model_selection import TimeSeriesSplit
from sklearn.pipeline import make_pipeline
from sklearn.externals import joblib

from dask_searchcv import GridSearchCV

from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
import dask_xgboost as dxgb

'''-------------------------------------------------------------------------------------------------------------------------'''
from collections import defaultdict

from sklearn.pipeline import make_pipeline

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator , MultipleLocator
from sklearn.model_selection import TimeSeriesSplit

from matplotlib.gridspec import GridSpec
import plotly.tools as tls
import plotly
import plotly.plotly as py
from pandas import DataFrame 

from scipy.stats import *
from astral import Astral
import datetime
import matplotlib.pyplot as plt
import warnings

plotly.tools.set_credentials_file(username='Furqan92', api_key='22DfVN5rFRg79OYygN5h')

tscv = TimeSeriesSplit(n_splits=5)
random_seed = 1234

## Replacing number in season by real names and in weathersit by description
def num_name(df):
    df = df.copy()
    season = {2:'spring', 3:'summer', 4:'fall', 1:'winter'}
    df['season']= df.season.apply(
               lambda x: season[x]).astype('category') 
    weathersit = {1:'Good', 2:'Acceptable', 3:'Bad', 4:'Chaos'}
    df['weathersit']= df.weathersit.apply(
               lambda x: weathersit[x]).astype('category') 
    return df

## Creating a new variable that compares the value to the past 7 days 
## the first 5 rows will be dropped if 'windspeed'is calculated and only 2 for the rest 

def relative_values(dataset, columns):
    dataset = dataset.copy()
    max = {'temp':41,'atemp':50,'hum':100,'windspeed':67}
    for i in columns:
        true=dataset[i]*max[i]
        avg7 = true.rolling(min_periods=1,window=24*7).mean().shift()
        std7 = true.rolling(min_periods=1,window=24*7).std().shift()
        name = 'relative_' + i 
        dataset[name]= (true - avg7)/std7
    dataset = dataset.replace([np.inf, -np.inf], np.nan).dropna()
    return dataset 
        
# Preperation for isDaylight()
city_name = 'Washington DC'
a = Astral()
a.solar_depression = 'civil'
city = a[city_name]
'''Feature Creation Functions'''





