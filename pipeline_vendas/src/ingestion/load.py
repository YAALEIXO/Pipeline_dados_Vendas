import pandas as pd
from pathlib import Path

def load_sales_data(file_path: str) -> pd.DataFrame:
    """
    Carrega dados de vendas a partir de um arquivo CSV.
    """
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    raw_path = Path(r"C:\Users\ANTONOV\Documents\Projeto\pipeline_vendas\data\raw\vendas.csv")
    df_sales = load_sales_data(raw_path)
    print(df_sales.head())
