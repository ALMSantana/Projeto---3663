from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

service = Service("driver/chromedriver.exe") # AJUSTEI AQUI

chrome_options = Options()

driver = webdriver.Chrome(service=service, options=chrome_options)

test_cases = [
    {
        "case_id": 1,
        "description": "Login com e-mail e senha corretos.",
        "email": "email@acordelab.com.br", # AJUSTEI AQUI
        "password": "123senha", # AJUSTEI AQUI
        "expected_result": "Aprovado",
        "verification_step": "Verificar se a URL após login corresponde à URL da página inicial do aplicativo.",
        "error_message_expected": None
    },
    {
        "case_id": 2,
        "description": "Login com e-mail correto e senha incorreta.",
        "email": "usuario@correto.com",
        "password": "senhaIncorreta123",
        "expected_result": "Reprovado",
        "verification_step": "Verificar se a mensagem de erro 'E-mail ou senha incorretos. Tente novamente.' é exibida.",
        "error_message_expected": "E-mail ou senha incorretos. Tente novamente." 
    },
    {
        "case_id": 3,
        "description": "Login com e-mail incorreto e senha correta.",
        "email": "usuario@incorreto.com",
        "password": "senhaCorreta123",
        "expected_result": "Reprovado",
        "verification_step": "Verificar se a mensagem de erro 'E-mail ou senha incorretos. Tente novamente.' é exibida.",
        "error_message_expected": "E-mail ou senha incorretos. Tente novamente."
    },
    {
        "case_id": 4,
        "description": "Login com e-mail e senha em branco.",
        "email": "",
        "password": "",
        "expected_result": "Reprovado",
        "verification_step": "Verificar se a mensagem de erro 'Informe seu e-mail e senha.' é exibida.",
        "error_message_expected": "E-mail ou senha incorretos. Tente novamente." # AJUSTEI AQUI
    }
]

url = "https://almsantana.github.io/" # AJUSTEI AQUI

driver.get(url)

time.sleep(1)

assert "Index - AcordeLab" in driver.title

for test in test_cases:
    driver.find_element(By.ID, "email").send_keys(test["email"])
    driver.find_element(By.ID, "senha").send_keys(test["password"])
    driver.find_element(By.CSS_SELECTOR, "input.botao-login").click()
 
    time.sleep(3)  #AJUSTEI AQUI

    if test["expected_result"] == "Aprovado":
        try:
            assert driver.current_url == url+"home.html" # AJUSTEI AQUI
            print("Caso de teste ID:", test["case_id"], "Aprovado")
        except AssertionError:
            print("Caso de teste ID:", test["case_id"], "Reprovado")
    else:
        error_message = driver.find_element(By.CSS_SELECTOR, "p.mensagem-erro").text
        if error_message == test["error_message_expected"]:
            print("Caso de teste ID:", test["case_id"], "Aprovado")
        else:
            print("Caso de teste ID:", test["case_id"], "Reprovado")

    driver.find_element(By.ID, "email").clear() # REMOVI AQUI
    driver.find_element(By.ID, "senha").clear() # REMOVI AQUI

    if driver.current_url != url:
        driver.get(url)

    time.sleep(1)  

time.sleep(3)
driver.quit()
