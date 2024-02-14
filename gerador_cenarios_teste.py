from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_cenario_teste(caso_uso):
    prompt_sistema = f""""
        Você é um especialista em desenvolver cenários de teste para validar uma aplicação web, quanto sua navegação.
        Para isso, considere o caso de uso destacado em: {caso_uso}.

        Seu caso de teste deve fornecer dados suficientes para validar uma aplicação HTML, CSS e JS e para que
        possa ser implementado usando Python e Selenium.
    """

    resposta = cliente.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_sistema}
        ],
        temperature=0.5
    )

    return resposta.choices[0].message.content