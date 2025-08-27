def standardize_datatypes(df):
    for column in df.columns:
        # Try converting string dates to datetime
        if df[column].dtype == 'object':
            try:
                df[column] = pd.to_datetime(df[column])
                print(f"Converted {column} to datetime")
            except ValueError:
                # Try converting to numeric if datetime fails
                try:
                    df[column] = pd.to_numeric(df[column].str.replace('$', '').str.replace(',', ''))
                    print(f"Converted {column} to numeric")
                except:
                    pass
  return df
