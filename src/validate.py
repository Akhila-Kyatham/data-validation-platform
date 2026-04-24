def row_count_check(source_df, target_df):
    return len(source_df) == len(target_df)

def schema_check(df, expected_columns):
    return list(df.columns) == expected_columns

def null_check(df):
    return df.isnull().sum().sum() == 0