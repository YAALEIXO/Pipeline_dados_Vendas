from sqlalchemy import create_engine
from urllib.parse import quote_plus

def get_sqlserver_engine(
    server: str,
    database: str
):
    connection_string = (
        "mssql+pyodbc://@"
        f"{server}/{database}"
        "?driver=" + quote_plus("ODBC Driver 17 for SQL Server") +
        "&trusted_connection=yes"
    )

    engine = create_engine(connection_string)
    return engine
