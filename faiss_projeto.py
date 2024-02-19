from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os
import json
from gerador_embedding import *
import numpy as np
import faiss

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

FAISS_INDEX_SIZE = 1536 #para text-embedding-3-small,já para text-embedding-3-large 3072
DIRETORIO_DOCUMENTOS = "AcordeLab"
CAMINHO_DADOS_FAISS = "projeto.index" 
CAMINHO_METADADOS = "metadados_projeto.json"

def ler_criar_indice_faiss(caminho_arquivo, tamanho_dimensoes):
    if os.path.exists(caminho_arquivo):
        print("\nÍndice já existe, carregando...")
        return faiss.read_index(caminho_arquivo)
    else:
        print("\nCriando novo índice...")
        return faiss.IndexFlatL2(tamanho_dimensoes)

def criar_dados_faiss(caminho_dados_faiss, descricoes, metadados, caminho_metadados):
    dados_faiss = ler_criar_indice_faiss(caminho_dados_faiss, FAISS_INDEX_SIZE)

    if not os.path.exists(caminho_dados_faiss):
        dados_faiss = adicionar_indice_embedding(dados_faiss, descricoes, metadados, caminho_metadados)
        faiss.write_index(dados_faiss, caminho_dados_faiss)

    return dados_faiss

def adicionar_indice_embedding(dados_faiss, descricoes, metadados, caminho_metadados):
    embeddings = np.array([gerar_embedding(texto) for texto in descricoes]).astype('float32')
    faiss.normalize_L2(embeddings)
    dados_faiss.add(embeddings)

    with open(caminho_metadados, 'w', encoding='utf-8') as arquivo_saida:
        json.dump(metadados, arquivo_saida, ensure_ascii=False)

    return dados_faiss

def buscar_documento_similar(texto_consultado, dados_faiss, caminho_metadados, qtd_resultados = 1):
    texto_consultado_embedding = np.array([gerar_embedding(texto_consultado)]).astype('float32')
    faiss.normalize_L2(texto_consultado_embedding)
    D, I = dados_faiss.search(texto_consultado_embedding, qtd_resultados)

    with open(caminho_metadados, encoding='utf-8') as arquivo_entrada:
        metadados = json.load(arquivo_entrada)

    for i in range(qtd_resultados):
        indice = I[0][i]
        print(f"\nSimilaridade {i+1}: {D[0][i]}")
        print(f"Documento: {metadados[indice]['documento']}")
        print(f"Texto: {metadados[indice]['meta_descricao']}")

    caminho_documento_escolhido = ""

    if metadados[I[0][0]].get("caminho"):
        caminho_documento_escolhido = metadados[I[0][0]].get("caminho") 
    
    return caminho_documento_escolhido