import pandas as pd

def add_date_features(df: pd.DataFrame, date_col='Date') -> pd.DataFrame:
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col).reset_index(drop=True) 

    df['Year'] = df[date_col].dt.year
    df['Month'] = df[date_col].dt.month
    df['Day'] = df[date_col].dt.day

    return df


def add_return(df: pd.DataFrame, price_col='Price') -> pd.DataFrame:
    df['Return'] = df[price_col].pct_change()
    return df


def feature_pipeline(df: pd.DataFrame) -> pd.DataFrame:

    df = add_date_features(df, 'Date')

    df = add_return(df, 'Price')

    return df