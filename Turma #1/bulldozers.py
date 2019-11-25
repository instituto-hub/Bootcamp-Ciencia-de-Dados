import pandas as pd
import numpy as np
from fastai_utils import add_datepart, train_cats, proc_df
import os
import math
from sklearn.ensemble import RandomForestRegressor


PATH = "data/bulldozers/"
dep = 'SalePrice'

df_raw = pd.read_csv(f'{PATH}Train.csv', low_memory=False,
                     parse_dates=["saledate"])


def rmse(x,y): return math.sqrt(((x-y)**2).mean())


def print_score(m):
    res = [rmse(m.predict(X_train), y_train), rmse(m.predict(X_valid), y_valid),
                m.score(X_train, y_train), m.score(X_valid, y_valid)]
    if hasattr(m, 'oob_score_'): res.append(m.oob_score_)
    print(res)


def split_vals(a,n): return a[:n].copy(), a[n:].copy()


def display_all(df):
    with pd.option_context("display.max_rows", 1000, "display.max_columns", 1000):
        print(df)

#display_all(df_raw.describe(include='all').T)

df_raw.SalePrice = np.log(df_raw.SalePrice)

df_raw = add_datepart(df_raw, 'saledate')

train_cats(df_raw)

os.makedirs('tmp', exist_ok=True)
df_raw.to_feather('tmp/bulldozers-raw')

df, y, nas = proc_df(df_raw, 'SalePrice')

n_valid = 12000  # same as Kaggle's test set size
n_trn = len(df)-n_valid
raw_train, raw_valid = split_vals(df_raw, n_trn)
X_train, X_valid = split_vals(df, n_trn)
y_train, y_valid = split_vals(y, n_trn)

m = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features=0.5, n_jobs=-1, oob_score=True)

m.fit(X_train, y_train)
print_score(m)
