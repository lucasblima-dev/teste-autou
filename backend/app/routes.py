from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .services.ai_validator import process_email

router = APIRouter()

class EmailInput(BaseModel):
  text: str

@router.post("/classify", status_code=200)
def classify_email_endpoint(email: EmailInput):
  if not email.text or not email.text.strip():
    raise HTTPException(status_code=400, detail="O campo 'text' não pode estar vazio.")
    
  try:
    result = process_email(email.text)
    return result
  except Exception as e:
    print(f"Erro no processamento: {e}") 
    raise HTTPException(status_code=500, detail=f"Erro: {str(e)}")