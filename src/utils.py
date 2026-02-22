def assert_no_na(df, cols):
    for col in cols:
        assert df[col].isna().sum() == 0, f"NA found in {col}"


def assert_positive(df, cols):
    for col in cols:
        assert (df[col] >= 0).all(), f"Negative values found in {col}"


def validate_pipeline(df):

    assert_no_na(df, ['Price', 'Open', 'High', 'Low', 'Change %'])
    assert_positive(df, ['Price', 'Open', 'High', 'Low'])