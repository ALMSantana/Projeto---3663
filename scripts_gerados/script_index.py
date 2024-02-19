```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Inicia o serviço do Chrome
service = Service()

# Configurações opcionais para o Chromium.
chrome_options = Options()
# Insira aqui qualquer configuração adicional desejada com chrome_options.add_argument

# Instancia o webdriver com as opções definidas
driver = webdriver.Chrome(service=service, options=chrome_options)

# Casos de teste
test_cases = [
    {
        "case_id": 1,
        "description": "Login com e-mail e senha corretos.",
        "email": "usuario@correto.com",
        "password": "senhaCorreta123",
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
        "error_message_expected": "Informe seu e-mail e senha."
    }
]

# URL da aplicação
url = "URL_DA_APLICACAO"

# Abre a URL no navegador
driver.get(url)

# Espera para garantir que a página carregou
time.sleep(1)

assert "Index - AcordeLab" in driver.title

for test in test_cases:
    # Preenche o e-mail e a senha conforme o caso de teste
    driver.find_element(By.ID, "email").send_keys(test["email"])
    driver.find_element(By.ID, "senha").send_keys(test["password"])
    driver.find_element(By.CSS_SELECTOR, "input.botao-login").click()

    time.sleep(1)  # Espera para a ação ser processada

    # Verificação e lógica de validação de acordo com o caso de teste
    if test["expected_result"] == "Aprovado":
        try:
            # Este é um placeholder da URL esperada. Adicione a URL específica do seu teste.
            assert driver.current_url == "URL_ESPERADA"
            print("Caso de teste ID:", test["case_id"], "Aprovado")
        except AssertionError:
            print("Caso de teste ID:", test["case_id"], "Reprovado")
    else:
        error_message = driver.find_element(By.CSS_SELECTOR, "p.mensagem-erro").text
        if error_message == test["error_message_expected"]:
            print("Caso de teste ID:", test["case_id"], "Aprovado")
        else:
            print("Caso de teste ID:", test["case_id"], "Reprovado")

    # Limpa os campos para o próximo teste
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "senha").clear()

    # Retorna para a página de login se a aplicação redirecionou para outra página após o login
    if driver.current_url != url:
        driver.get(url)

    time.sleep(1)  # Intervalo entre os testes

# Encerra o navegador com uma pausa antes do fechamento
time.sleep(3)
driver.quit()
```

Troque "URL_DA_APLICACAO" pela URL real onde o aplicativo está hospedado. Substitua "URL_ESPERADA" pela URL que deveria ser acessada após um login bem-sucedido. Os comentários em português estão incluídos para facilitar o entendimento do script.