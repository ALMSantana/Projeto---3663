from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def criar_lista_ids_app_web(diretorio = "AcordeLab"):
    lista_ids_arquivos = []
    dicionario_arquivos = {}

    for caminho_diretorio, nomes_diretorios, nomes_arquivos in os.walk(diretorio):
        arquivos_web = [f for f in nomes_arquivos if f.endswith(('.html', '.css', '.js'))]
        
        for arquivo in arquivos_web:
            caminho_completo = os.path.join(caminho_diretorio, arquivo)
            with open(caminho_completo, 'rb') as arquivo_aberto:
                web_file = cliente.files.create(
                    file=arquivo_aberto,
                    purpose="assistants"
                )
                lista_ids_arquivos.append(web_file.id)
                dicionario_arquivos[arquivo] = web_file.id

    caminho_arquivo = "documentos/exemplos_caso_uso.txt"
    nome_arquivo = os.path.basename(caminho_arquivo)
    arquivo_exemplo_caso = cliente.files.create(
        file=open(caminho_arquivo, "rb"),
        purpose="assistants"
    )

    lista_ids_arquivos.append(arquivo_exemplo_caso.id)
    dicionario_arquivos[nome_arquivo] = arquivo_exemplo_caso.id

    return lista_ids_arquivos, dicionario_arquivos
