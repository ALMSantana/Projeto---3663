MODELO_REFINADO = "ft:gpt-3.5-turbo-1106:alura-content::8sFPyajg"
MODELO_GPT_3_5 = "gpt-3.5-turbo"
MODELO_GPT_4 = "gpt-4-0125-preview"
MODELO_EMBEDDING = "text-embedding-3-small"

STATUS_COMPLETED = "completed" 
STATUS_FAILED = "failed"

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")
