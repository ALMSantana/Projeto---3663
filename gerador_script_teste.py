from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os
from criador_usuarios_de_teste import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_script_teste(cenario_teste, documento, dicionario_arquivos, assistente, thread, modelo=MODELO_GPT_4):
    usuarios_teste = criar_usuarios_teste(cenario_teste=cenario_teste, documento=documento, dicionario=dicionario_arquivos)
    print("\nUsuários Gerados com o modo JSON:\n", usuarios_teste)
    pergunta = f""""
        Você é um especialista em gerar scripts de teste para elaboração de casos de uso e cenários de teste.

        Seu cenário de teste deve fornecer um script em Selenium e deve utilizar o chromium como driver para isso
        Além disso, seu código deve ser escrito em Python e deve utilizar apenas as bibliotecas em destaque.
        Dando uma pausar de 3 segundos antes de fechar o script.

        # Bibliotecas

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        import time

        # Arquivos que farão parte do teste

        Consulte nos arquivos internos os documentos: {dicionario_arquivos[documento+".html"]}, {dicionario_arquivos[documento+".css"]}  e {dicionario_arquivos[documento+".js"]}

        Além disso, considere o {cenario_teste} para elaborar o teste em selenium.

        Considere também inserir quatro (4) casos de teste, utilizando os resultados de     {usuarios_teste}. Faça as iterações em um laço de repetição, mostrando ao final "Aprovado" se o teste deveria logar e logou ou deveria falhar e falhou.

        # Saída

        Apenas um script em python com comentários em português para auxiliar a pessoa desenvolvedora
    """
    
    cliente.beta.threads.messages.create(
        thread_id=thread.id, 
        role = "user",
        content =  pergunta
    )

    run = cliente.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistente.id,
        tools=[{"type":"retrieval"}],
        model=modelo
    )

    ran = cliente.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    while ran.status != STATUS_COMPLETED:
        print("Gerando Script: ", ran.status)
        ran = cliente.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

        if ran.status == STATUS_FAILED:
            raise Exception("OpenAI Falhou!")
        
    mensagens = cliente.beta.threads.messages.list(
        thread_id = thread.id
    )
    
    return mensagens.data[0].content[0].text.value