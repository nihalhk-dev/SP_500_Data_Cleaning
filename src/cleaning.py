import pandas as pd


def fix_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip()
    return df


def convert_date(df: pd.DataFrame, date_col='Date') -> pd.DataFrame:
    df[date_col] = pd.to_datetime(df[date_col])
    return df


def drop_unused_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    return df.drop(columns=cols, errors='ignore')


def convert_numeric_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    for col in cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(',', '', regex=False)
            .str.replace('%', '', regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def fill_missing_prices(df: pd.DataFrame, col='Price') -> pd.DataFrame:
    df = df.sort_values('Date').reset_index(drop=True)
    df[col] = df[col].interpolate(method='linear')
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)


def fix_ohlc_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensures OHLC structural integrity:
    High >= max(Open, Price)
    Low <= min(Open, Price)
    """

    df['High'] = df[['High', 'Open', 'Price']].max(axis=1)
    df['Low'] = df[['Low', 'Open', 'Price']].min(axis=1)

    return df


def remove_extreme_return_outliers(
    df: pd.DataFrame,
    price_col='Price',
    threshold=0.2
) -> pd.DataFrame:

    df = df.sort_values('Date').reset_index(drop=True)

    returns = df[price_col].pct_change()

    outlier_mask = returns.abs() > threshold

    df.loc[outlier_mask, price_col] = None

    df[price_col] = df[price_col].ffill()

    return df.reset_index(drop=True)


def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:

    df = fix_column_names(df)

    df = convert_date(df, 'Date')

    df = drop_unused_columns(df, ['Vol.'])

    numeric_cols = ['Price', 'Open', 'High', 'Low', 'Change %']
    df = convert_numeric_columns(df, numeric_cols)

    df = fill_missing_prices(df, 'Price')

    df = remove_duplicates(df)

    df = fix_ohlc_anomalies(df)

    df = remove_extreme_return_outliers(df, 'Price')

    return df