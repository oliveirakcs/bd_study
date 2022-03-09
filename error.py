from sqlalchemy import create_engine, engine
import pandas as pd

engine = create_engine('sqlite://', echo=False)

arquivo = pd.read_csv('teste.csv')
arquivo.to_parquet('output.parquet')

t = pd.read_parquet('output.parquet', engine = 'fastparquet', index = False)

t.to_sql('dw_table', engine)

a = engine.execute("SELECT * FROM dw_table")


