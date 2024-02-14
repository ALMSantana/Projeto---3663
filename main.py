from gerador_casos_uso import *
from gerador_cenarios_teste import *
from gerador_script_teste import *

def main():
    casos_uso = gerar_caso_uso()
    print("\nCaso de Uso:\n", casos_uso)


if __name__ == "__main__":
    main()