from typing import Iterable
import toolz.curried
import pandas as pd


@toolz.curry
def to_string(cols: Iterable, df: pd.DataFrame) -> pd.DataFrame:
    li = list(df)
    for col in cols:
        if col in li:
            df[[col]] = df[[col]].astype('str')
    return df


@toolz.curry
def to_int(cols: Iterable, df: pd.DataFrame) -> pd.DataFrame:
    li = list(df)
    for col in cols:
        if col in li:
            df[[col]] = df[[col]].astype('int')
    return df


@toolz.curry
def to_float(cols: Iterable, df: pd.DataFrame) -> pd.DataFrame:
    li = list(df)
    for col in cols:
        if col in li:
            df[[col]] = df[[col]].astype('float')
    return df


@toolz.curry
def to_date(cols: Iterable, df: pd.DataFrame) -> pd.DataFrame:
    li = list(df)
    for col in cols:
        if col in li:
            df[col] = pd.to_datetime(df[col]).apply(lambda x: x.date())
    return df


@toolz.curry
def to_datetime(cols: Iterable, df: pd.DataFrame) -> pd.DataFrame:
    li = list(df)
    for col in cols:
        if col in li:
            df[col] = pd.to_datetime(df[col])
    return df


@toolz.curry
def as_type(d: dict, df: pd.DataFrame) -> pd.DataFrame:
    for key, cols in d.items():
        if key == 'str':
            df = to_string(cols, df)
        if key == 'int':
            df = to_float(cols, df)
        if key == 'float':
            df = to_float(cols, df)
        if key == 'date':
            df = to_date(cols, df)
        if key == 'datetime':
            df = to_datetime(cols, df)
        return df


def to_dict(df: pd.DataFrame) -> dict:
    return df.to_dict('records')
