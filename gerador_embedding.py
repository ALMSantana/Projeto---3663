from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os
import json

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_embedding(texto, modelo = MODELO_EMBEDDING):
    return cliente.embeddings.create(
        input=texto,
        model= modelo
    ).data[0].embedding

def gerar_meta_descricao(documento, nome_arquivo, modelo = MODELO_GPT_4):
    prompt_sistema = f""""
        Analise o documento fornecido e gere um resumo conciso do seu conteúdo. 
        O documento pode ser uma página web com HTML, CSS, e JavaScript, detalhando 
        aspectos como design, funcionalidades interativas e informações específicas,
        ou um arquivo de texto com orientações e exemplos. O resumo deve capturar 
        os elementos centrais e o propósito do documento, destacando 
        características chave e tecnologias utilizadas. Este resumo será usado 
        para criar um embedding, otimizando a recuperação do documento em um 
        banco de dados vetorial.

        Sua meta-descrição deve incluir:

        - Nome do Arquivo: {nome_arquivo}
        - Propósito do Arquivo: Enfatise a ação principal do usuário do arquivo de acordo com o conteúdo. Não mencione outros tipos de linguagem a não ser a utilizada para escrever o documento. Disponível no arquivo {nome_arquivo}.
        - Tipo de Arquivo: HTML, CSS ou JS (escolha com base na linguagem usada)

        Como saída gere apenas a MetaDescrição que será utilizada para gerar embeddings.
    """

    prompt_usuario = f"Gere uma meta-descrição para o documento: {documento}"

    resposta = cliente.chat.completions.create(
        model=modelo,
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": prompt_usuario}
        ],
        temperature=0.5
    )

    return resposta.choices[0].message.content

def resgatar_documentos(caminho_metadados):
    json_string = carrega(caminho_metadados)
    json_metadados = json.loads(json_string)

    descricoes = []
    metadados = []

    for objeto in json_metadados:
        descricoes.append(objeto["meta_descricao"])
        metadados.append(objeto)
    
    return descricoes, metadados

def processar_documentos(diretorio_documentos="AcordeLab"):
    print("Processando documentos ...")

    extensoes_permitidas = ('.html', '.css', '.js')
    metadados = []
    descricoes = []

    for dirpath, dirnames, filenames in os.walk(diretorio_documentos):
        for arquivo in filenames:
            if arquivo.endswith(extensoes_permitidas):
                caminho_completo = os.path.join(dirpath, arquivo)
                with open(caminho_completo, 'r', encoding='utf-8') as arquivo_lido:
                    texto_completo = arquivo_lido.read()
                meta_descricao = gerar_meta_descricao(documento=texto_completo, nome_arquivo=arquivo)
                metadados.append({'documento': arquivo, 'meta_descricao': meta_descricao, 'caminho': caminho_completo})
                descricoes.append(meta_descricao)

    return descricoes, metadados
