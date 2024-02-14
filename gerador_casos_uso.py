from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_caso_uso():
    prompt_sistema = f""""
        Você é um especialista em desenvolver casos de uso. Você deve adotar o padrão abaixo para gerar seu caso de uso:

         *Nome da Persona*, em *contexto do app*, precisa realizar *tarefa no app* no aplicativo. Logo, *Beneficio Esperado*, para isso ela *descrição detalhada da tarefa realizada*.

        Considere os dados de entrada sugeridos pelo usuário e gere o caso de uso no formato adequado.
    """

    prompt_usuario = """"
        Ana deseja realizar login na plataforma AcordeLab.
    """

    resposta = cliente.chat.completions.create(
        model="ft:gpt-3.5-turbo-1106:alura-content::8sF0kA99",
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": prompt_usuario}
        ],
        temperature=0.5
    )

    return resposta.choices[0].message.content