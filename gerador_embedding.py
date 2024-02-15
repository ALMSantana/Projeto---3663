from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_embedding(texto, modelo = MODELO_EMBEDDING):
    return cliente.embeddings.create(
        input=texto,
        model= modelo
    )

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
        - Propósito do Arquivo: Enfatise a ação principal do usuário do arquivo de acordo com o conteúdo
        - Tipo de Arquivo: HTML, CSS ou JS

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