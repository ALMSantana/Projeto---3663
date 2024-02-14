from gerador_casos_uso import *
from gerador_cenarios_teste import *
from gerador_script_teste import *
from tools import *

def main():
    pedido_usuario = input("Digite um caso de uso: ")

    casos_uso = gerar_caso_uso(pedido_usuario, MODELO_GPT_3_5)
    print("\nCaso de Uso - Não Refinado:\n", casos_uso)

    casos_uso = gerar_caso_uso(pedido_usuario, MODELO_REFINADO)
    print("\nCaso de Uso - Refinado:\n", casos_uso)


if __name__ == "__main__":
    main()