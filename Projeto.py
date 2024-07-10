import os
from fastapi import FastAPI, HTTPException
from google.cloud import bigquery

# Configura o caminho para o arquivo de credenciais do BigQuery
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Aluno\\Desktop\\Projeto\\eternal-seeker-417314-36dc2f8fb2d1.json"

app = FastAPI()

# Inicializa o cliente do BigQuery
client = bigquery.Client()

@app.get("/")
async def root():
    return {"message": "API para executar a query SELECT * FROM teste.example_table"}

@app.get("/execute-query")
async def execute_query():
    query = "SELECT * FROM `teste.example_table`"
    try:
        query_job = client.query(query)
        results = query_job.result()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    rows = [dict(row) for row in results]
    return rows

