from fastapi import FastAPI
from app.api.routes import router as math_router
from app.db.database import create_db_and_tables
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Math Microservice")

Instrumentator().instrument(app).expose(app)

@app.on_event("startup")
async def startup():
    create_db_and_tables()

app.include_router(math_router)
