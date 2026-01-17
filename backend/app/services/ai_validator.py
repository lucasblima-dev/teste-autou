import os
import time
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_KEY:
  print("HF_API_KEY não encontrada")

client = InferenceClient(token=HF_API_KEY)

MODELS = [
  "Qwen/Qwen2.5-72B-Instruct",
  "mistralai/Mistral-7B-Instruct-v0.3",
  "microsoft/Phi-3.5-mini-instruct"
]

def call_huggingface_chat(messages: list, max_retries: int = 3):
  for model in MODELS:
    for attempt in range(max_retries):
      try:
        print(f"Tentando modelo: {model} (Tentativa {attempt+1})")
        response = client.chat_completion(
          messages=messages,
          model=model,
          max_tokens=200, 
          stream=False
        )

        return response.choices[0].message.content
                
      except Exception as e:
        error_msg = str(e)
        print(f"Erro com {model}: {error_msg}")
        
        if "model_not_supported" in error_msg or "404" in error_msg:
          print(f"Modelo {model} indisponível. Pulando para o próximo...")
          break
        
        if "503" in error_msg or "loading" in error_msg.lower():
          wait_time = 20
          print(f"Modelo carregando... aguardando {wait_time}s.")
          time.sleep(wait_time)
        elif "429" in error_msg:
          print("Limite atingido. Aguardando 5s.")
          time.sleep(5)
        else:
          time.sleep(2)
                    
    print("Falha crítica: Nenhum modelo respondeu.")
    return None

def classify_text(text: str) -> str:
  messages = [
      {
          "role": "system", 
          "content": (
              "Você é um classificador de emails para uma empresa financeira. "
              "Classifique o email abaixo ESTRITAMENTE como 'Produtivo' ou 'Improdutivo'. "
              "Produtivo = requer ação, suporte, dúvidas ou atualização. "
              "Improdutivo = felicitações, spam ou agradecimentos. "
              "Responda APENAS a palavra da classificação."
          )
      },
      {
          "role": "user", 
          "content": f"Email: {text}"
      }
  ]
    
  result = call_huggingface_chat(messages)
    
  if not result: return "Indefinido"

  clean_result = result.strip().replace(".", "")

  if "Improdutivo" in clean_result: return "Improdutivo"
  if "Produtivo" in clean_result: return "Produtivo"
    
  return "Indefinido"

def generate_ai_response(text: str, category: str) -> str:
  if category == "Produtivo":
      instruction = "Escreva uma resposta formal confirmando o recebimento e dizendo que a equipe técnica analisará."
  else:
      instruction = "Escreva uma resposta curta e polida agradecendo o contato."

  messages = [
    {
      "role": "system", 
      "content": "Você é um assistente de suporte técnico útil e profissional da empresa AutoU."
    },
    {
      "role": "user", 
      "content": f"Tarefa: {instruction}\n\nEmail original recebido: '{text}'"
    }
  ]

  result = call_huggingface_chat(messages)

  return result if result else "Não foi possível gerar a resposta no momento."

def process_email(text: str) -> dict:
  category = classify_text(text)
  suggestion = generate_ai_response(text, category)

  return {"category": category, "suggestion": suggestion}