from ingestion.load import load_sales_data
from processing.ETL import tratamento_dados
from pathlib import Path
from utils.db_conection import get_sqlserver_engine
from loader_db.load_to_sqlserver import load_dataframe_to_sqlserver


def run_pipeline():
    
    raw_path = Path("pipeline_vendas/data/raw/vendas.csv")    
    processed_path = Path("pipeline_vendas/data/processed/vendas_tratadas.csv")    
    df = load_sales_data(raw_path)    
    df_clean = tratamento_dados(df)    
    processed_path.parent.mkdir(parents=True, exist_ok=True)    
    df_clean.to_csv(processed_path, index=False)    
    engine = get_sqlserver_engine(
        server="DESKTOP-OTNECLH\\SQLEXPRESS",
        database="DW"
    )

    load_dataframe_to_sqlserver(
        df=df_clean,
        engine=engine,
        table_name="vendas",
        schema="stg"
    )
   

    print("Pipeline executado com sucesso!")
   
    

if __name__ == "__main__":
    run_pipeline()