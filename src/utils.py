def validate_columns(df, required_columns):
    """
    Ensure required columns exist in dataframe.
    """
    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"❌ Missing required columns: {missing}")


def summarize_counts(df, column):
    """
    Return value counts for a column.
    """
    return df[column].value_counts(dropna=False)


def print_section(title):
    """
    Pretty section header for notebooks/scripts.
    """
    print("\n" + "=" * 60)
    print(title.upper())
    print("=" * 60)
