import matplotlib.pyplot as plt

def plot_price(df, date_col='Date', price_col='Price', title="Price over Time"):
    plt.figure(figsize=(10,4))
    plt.plot(df[date_col], df[price_col], marker='o', markersize=2)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_hist(df, col, bins=50, title=None):
    plt.figure(figsize=(8,4))
    plt.hist(df[col].dropna(), bins=bins)
    plt.title(title or f"{col} Distribution")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()