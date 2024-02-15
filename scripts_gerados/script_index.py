```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Configurações do driver do navegador
options = Options()
options.headless = False  # Executar o navegador em modo não visual (headless) ou não
service = Service(executable_path="/path/to/chromedriver")  # Atualize para o caminho do seu Chromedriver

# Inicializa o WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Define dados de teste
test_cases = [
    {
        "case_id": 1,
        "email": "email@acordelab.com.br",
        "senha": "123senha",
        "esperado": "aprovado",
        "mensagem_erro": ""
    },
    {
        "case_id": 2,
        "email": "incorrectemail@acordelab.com.br",
        "senha": "123senha",
        "esperado": "falho",
        "mensagem_erro": "E-mail ou senha incorretos. Tente novamente."
    },
    {
        "case_id": 3,
        "email": "email@acordelab.com.br",
        "senha": "wrongpassword",
        "esperado": "falho",
        "mensagem_erro": "E-mail ou senha incorretos. Tente novamente."
    },
    {
        "case_id": 4,
        "email": "",
        "senha": "",
        "esperado": "falho",
        "mensagem_erro": "Campos vazios. Tente novamente."
    },
]

for test_case in test_cases:
    # Navegar até a página de login
    driver.get("http://enderecodaaplicacao.com/login")
    
    # Preenche o campo de email
    email_field = driver.find_element(By.ID, "email")
    email_field.clear()
    email_field.send_keys(test_case["email"])
    
    # Preenche o campo de senha
    senha_field = driver.find_element(By.ID, "senha")
    senha_field.clear()
    senha_field.send_keys(test_case["senha"])
    
    # Clicar no botão 'Login'
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()
    
    time.sleep(1)  # Espera para que a ação de login possa ser processada
    
    # Verifica o resultado do teste
    try:
        mensagem_erro = driver.find_element(By.CSS_SELECTOR, ".mensagem-erro").text
        assert test_case["mensagem_erro"] == mensagem_erro
        resultado_teste = "falho" if mensagem_erro else "aprovado"
    except:
        resultado_teste = "aprovado"  # Se não encontrar a mensagem de erro, considera aprovado
    
    print(f"Caso de teste {test_case['case_id']}: {'Aprovado' if test_case['esperado'] == resultado_teste else 'Falho'}")
    
    time.sleep(3)  # Pausa antes do próximo caso de teste

# Fecha o navegador após a execução de todos os testes
driver.quit()
```