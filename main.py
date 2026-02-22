from src.io import load_csv, save_csv
from src.cleaning import drop_unused_columns, fix_column_names, fill_missing_prices, remove_duplicates, remove_outliers
from src.features import add_date_features, add_return
from src.utils import assert_no_na
from src.viz import plot_price, plot_hist
import pandas as pd

df = load_csv("data/raw/sp500_dirty.csv")

# Cleaning
df = fix_column_names(df)
df = drop_unused_columns(df, ['Vol.'])
df = fill_missing_prices(df, 'Price')
df = remove_duplicates(df)
df = remove_outliers(df, 'High')

# Feature engineering
df = add_date_features(df, 'Date')

# Convert and SORT (critical step)
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date').reset_index(drop=True)

# Now calculate returns correctly
df = add_return(df, 'Price')

# Validations
assert_no_na(df, ['Price', 'Open', 'High', 'Low', 'Change %'])

# Save clean dataset
save_csv(df, "data/processed/sp500_clean.csv")

# Visualizations
plot_price(df)
plot_hist(df, 'Price')
plot_hist(df, 'Return')