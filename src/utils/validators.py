def validate_columns(df, required_columns, source_name):
    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(
            f"{source_name} missing required columns: {missing}"
        )
