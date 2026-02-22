import pandas as pd

def drop_unused_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    return df.drop(columns=cols, errors='ignore')

def fix_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip() for col in df.columns]
    return df

def fill_missing_prices(df: pd.DataFrame, col='Price') -> pd.DataFrame:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col] = df[col].ffill()  # <--- usar ffill() directamente
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)

def remove_outliers(df: pd.DataFrame, col: str, factor=3) -> pd.DataFrame:
    mean = df[col].mean()
    std = df[col].std()
    df = df[(df[col] <= mean + factor*std) & (df[col] >= mean - factor*std)]
    return df.reset_index(drop=True)