from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import psutil

app = FastAPI(title="Dashboard de Monitoramento", version="1.0")

# Configuração de CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota da API que retorna o uso de CPU e Memória
@app.get("/api/stats")
def get_stats():
    cpu_usage = psutil.cpu_percent(interval=None)
    memory = psutil.virtual_memory()
    
    return {
        "cpu": cpu_usage,
        "memory": {
            "percent": memory.percent,
            "used": round(memory.used / (1024 ** 3), 2),  # Convertido para GB
            "total": round(memory.total / (1024 ** 3), 2)  # Convertido para GB
        }
    }

# Monta a pasta estática para servir o frontend (opcional, mas recomendado)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
