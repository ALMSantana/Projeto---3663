from gerador_casos_uso import *
from gerador_cenarios_teste import *
from gerador_script_teste import *
from tools import *

from assistente_projeto import *
import openai

def main():
    pedido_usuario = input("Digite um caso de uso: ")
    pagina_considerada = "index"

    try:
        lista_ids_arquivos, mapa_arquivos = criar_lista_ids_app_web_otimizado(pedido_usuario, diretorio="AcordeLab")
        assistente = criar_assistente(lista_ids_arquivos=lista_ids_arquivos)
        thread = criar_thread()

        casos_uso = gerar_caso_uso(prompt=pedido_usuario, assistente=assistente, thread=thread)
        print("\nCasos de Uso:\n", casos_uso)

        cenario_teste = gerar_cenario_teste(caso_uso=casos_uso, documento=pagina_considerada, dicionario_arquivos = mapa_arquivos,  assistente=assistente, thread=thread)
        print("\nCenário de Teste:\n", cenario_teste)

        script_teste = gerar_script_teste(cenario_teste=cenario_teste, documento=pagina_considerada, dicionario_arquivos = mapa_arquivos, assistente=assistente, thread=thread)
        print("\nScript de Teste\n", script_teste)

        salva(f"scripts_gerados/script_{pagina_considerada}.py", script_teste)
    except openai.APIError as e:
        print("Deu erro: ", e)
    finally:
        print("Apagando arquivos gerados ...")
        apagar_arquivos(lista_ids_arquivos=lista_ids_arquivos)
        apagar_assistente(assistant_id=assistente.id)
        apagar_thread(thread_id=thread.id)



if __name__ == "__main__":
    main()