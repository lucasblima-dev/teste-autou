from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router as api_router

def create_app():
  app = FastAPI(
      title="AutoU API de Classificação de E-mail",
      description="Uma API para classificar e-mails e sugerir respostas usando IA.",
      version="1.0.0"
  )

  origins = [
      "http://localhost",
      "http://localhost:5173",
      "https://autou-frontend-fkvu.onrender.com"
  ]

  app.add_middleware(
      CORSMiddleware,
      allow_origins=origins,
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )

  app.include_router(api_router, prefix="/api")

  @app.get("/", tags=["Health Check"])
  def read_root():
    return {"status": "API is running!"}

  return app