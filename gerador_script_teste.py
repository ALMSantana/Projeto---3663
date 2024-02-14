from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_script_teste(caso_uso, cenario_teste):
    documento_empresa = carrega("documentos/acorde_lab.txt")

    prompt_sistema = f""""
        Você é um especialista em gerar scripts de teste para elaboração de casos de uso e cenários de teste.
        Considere o contexto da empresa disponível em: {documento_empresa}

        Seu cenário de teste deve fornecer um script em Selenium e deve utilizar o chromium como driver para isso
        Além disso, seu código deve ser escrito em Python e deve utilizar apenas as bibliotecas em destaque.
        Dando uma pausar de 3 segundos antes de fechar o script.
        Não use headless.

        # Bibliotecas

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        import time
    """

    prompt_usuario = f"""
        Considere o caso de uso {caso_uso} e o cenário de teste {cenario_teste}.

        Crie um script para gerar um teste automatizado para ambos.
    """

    resposta = cliente.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": prompt_usuario}
        ],
        temperature=0.5
    )

    return resposta.choices[0].message.content