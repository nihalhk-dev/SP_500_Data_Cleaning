import pandas as pd

def add_date_features(df: pd.DataFrame, date_col='Date') -> pd.DataFrame:
    df[date_col] = pd.to_datetime(df[date_col])
    df['Year'] = df[date_col].dt.year
    df['Month'] = df[date_col].dt.month
    df['Day'] = df[date_col].dt.day
    return df

def add_return(df: pd.DataFrame, price_col='Price') -> pd.DataFrame:
    df['Return'] = df[price_col].pct_change()
    return df