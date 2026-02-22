import pandas as pd

def fix_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip() for col in df.columns]
    return df


def drop_unused_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    return df.drop(columns=cols, errors='ignore')


def convert_numeric_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def fill_missing_prices(df: pd.DataFrame, col='Price') -> pd.DataFrame:
    df[col] = df[col].ffill()
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)


def remove_outliers(df: pd.DataFrame, col: str, factor=3) -> pd.DataFrame:
    mean = df[col].mean()
    std = df[col].std()
    df = df[(df[col] <= mean + factor * std) &
            (df[col] >= mean - factor * std)]
    return df.reset_index(drop=True)


def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:

    df = fix_column_names(df)

    df = drop_unused_columns(df, ['Vol.'])

    numeric_cols = ['Price', 'Open', 'High', 'Low', 'Change %']
    df = convert_numeric_columns(df, numeric_cols)

    df = fill_missing_prices(df, 'Price')

    df = remove_duplicates(df)

    df = remove_outliers(df, 'High')

    return df