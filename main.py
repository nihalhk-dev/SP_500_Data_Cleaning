from src.io import load_csv, save_csv
from src.cleaning import clean_pipeline
from src.features import feature_pipeline
from src.utils import validate_pipeline
from src.viz import visualization_pipeline


RAW_PATH = "data/raw/sp500_dirty.csv"
PROCESSED_PATH = "data/processed/sp500_clean.csv"


def main():

    df = load_csv(RAW_PATH)

    df = clean_pipeline(df)

    df = feature_pipeline(df)

    validate_pipeline(df)

    save_csv(df, PROCESSED_PATH)

    visualization_pipeline(df)


if __name__ == "__main__":
    main()