from gerador_casos_uso import *
from gerador_cenarios_teste import *

def main():
    casos_uso = gerar_caso_uso()
    print("\nCaso de Uso:\n", casos_uso)

    cenario_teste = gerar_cenario_teste(caso_uso=casos_uso)
    print("\nCenario Teste\n", cenario_teste)

if __name__ == "__main__":
    main()