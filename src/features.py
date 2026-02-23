import pandas as pd

def add_date_features(df: pd.DataFrame, date_col='Date') -> pd.DataFrame:
    df = df.copy()

    df[date_col] = pd.to_datetime(df[date_col])

    df = df.sort_values(date_col).reset_index(drop=True)

    df['Year'] = df[date_col].dt.year
    df['Month'] = df[date_col].dt.month
    df['Day'] = df[date_col].dt.day

    return df

def add_return(df: pd.DataFrame, price_col='Price') -> pd.DataFrame:
    df = df.copy()

    df['Return'] = df[price_col].pct_change()

    return df

def add_rolling_features(df: pd.DataFrame,
                         price_col='Price',
                         return_col='Return') -> pd.DataFrame:
    df = df.copy()

    df['MA_20'] = df[price_col].rolling(window=20).mean()
    df['MA_50'] = df[price_col].rolling(window=50).mean()

    df['Volatility_20'] = df[return_col].rolling(window=20).std()

    return df

def feature_pipeline(df: pd.DataFrame) -> pd.DataFrame:

    df = add_date_features(df, 'Date')

    df = add_return(df, 'Price')

    df = add_rolling_features(df)

    return df