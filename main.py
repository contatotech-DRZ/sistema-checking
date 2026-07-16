from fastapi import FastAPI
from fastapi.staticfile import StaticFiles
import psutil

app = FastAPI()

@app.get("/api/stats")
async def get_stats():
       return{
              "cpu": psutil.cpu_percent(interval=1),
              "ram": psutil.virtual_memory().percent
       }

app.mount("/", StaticFiles(directory="static", html=True), name="static")