import matplotlib.pyplot as plt


def plot_price(df, date_col='Date', price_col='Price'):
    plt.figure(figsize=(12, 5))
    plt.plot(df[date_col], df[price_col])
    plt.title("S&P 500 Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_hist(df, col, bins=50):
    plt.figure(figsize=(8, 4))
    plt.hist(df[col].dropna(), bins=bins)
    plt.title(f"{col} Distribution")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


def visualization_pipeline(df):
    plot_price(df)
    plot_hist(df, 'Price')
    plot_hist(df, 'Return')