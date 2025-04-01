from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("../data/Relatorio_cadop.csv", sep=";", encoding="utf8")

@app.get("/operadora/buscar")
def buscar_por_razao_social(q: str = Query(..., min_length=1)):
    resultados = df[df["Razao_Social"].str.contains(q, case=False, na=False)]
    resultados = resultados.head(20).replace({np.nan: None})
    return resultados.to_dict(orient="records")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
