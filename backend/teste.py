import os
from app.services.ai_validator import process_email

email1 = "Prezados, o sistema está fora do ar e preciso emitir uma nota fiscal urgente. Aguardo retorno."
email2 = "Feliz Natal para toda a equipe da AutoU! ;)"

print(f"\nTestando e-mail Produtivo:\n'{email1}'")
try:
  resultado1 = process_email(email1)
  print(f"Resultado: {resultado1}")
except Exception as e:
  print(f"Erro: {e}")

print(f"\nTestando e-mail Improdutivo:\n'{email2}'")
try:
  resultado2 = process_email(email2)
  print(f"Resultado: {resultado2}")
except Exception as e:
  print(f"Erro: {e}")
