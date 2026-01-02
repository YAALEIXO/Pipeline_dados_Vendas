from ingestion.load import load_sales_data
from processing.ETL import tratamento_dados
from pathlib import Path

def run_pipeline():
    raw_path = Path("pipeline_vendas/data/raw/vendas.csv")
    processed_path = Path("pipeline_vendas/data/processed/vendas_tratadas.csv")

    df = load_sales_data(raw_path)
    df_clean = tratamento_dados(df)

    processed_path.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(processed_path, index=False)

    print("Pipeline executado com sucesso!")

if __name__ == "__main__":
    run_pipeline()