import pandas as pd

def validate_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Valida e limpa dados de vendas.
    - Remove registros sem produto
    - Remove quantidades ou preços inválidos
    """
    df = df.dropna(subset=["produto"])
    df = df[(df["quantidade"] > 0) & (df["preco_unitario"] > 0)]
    return df
