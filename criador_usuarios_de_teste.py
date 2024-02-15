from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def criar_usuarios_teste(cenario_teste, documento, dicionario, modelo = MODELO_GPT_4):
    prompt_sistema = f"""
    Você deve gerar um conjunto de dados de teste em formato JSON que serão utilizados
    com Selenium e Python para simular e aprovar a navegabilidade de uma aplicação.
    
    Consulte os arquivos {dicionario[documento+".js"]}, {dicionario[documento+".html"]}, e {dicionario[documento+".css"]} para verificar os dados corretos de autenticação. 
    
    Gere quatro casos distintos de teste, com apenas um deles resultando em 'Aprovado'.
    Lembre-se de que os dados gerados devem ser em formato JSON válido.
    
    Inclua explicitamente na sua resposta o formato JSON esperado para os casos de teste.
    """

    resposta = cliente.chat.completions.create(
        model=modelo,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "Você é um assistente útil projetado para gerar saídas em formato JSON. " + prompt_sistema},
            {"role": "user", "content": cenario_teste}
        ]
    )

    return resposta.choices[0].message.content