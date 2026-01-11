import pandas as pd

def load_dataframe_to_sqlserver(
    df: pd.DataFrame,
    engine,
    table_name: str,
    schema: str
):
    df.to_sql(
        name=table_name,
        con=engine,
        schema=schema,
        if_exists="append",
        index=False
    )
