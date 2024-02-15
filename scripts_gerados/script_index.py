# Importando as bibliotecas necessárias para o teste
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


service = Service(executable_path="driver/chromedriver.exe")  # Substitua "/path/to/chromedriver" pelo caminho do seu chromedriver

# Instancia o navegador
driver = webdriver.Chrome(service=service)

# Passo 1: Abrir o navegador e carregar a página de login da plataforma AcordeLab
driver.get("https://almsantana.github.io/")  # Substitua "URL da plataforma AcordeLab" pela URL real da página de login

# Passo 2: Verificar se os campos de email e senha estão presentes
assert driver.find_element(By.ID, "email").is_displayed(), "Campo de e-mail não está presente"
assert driver.find_element(By.ID, "senha").is_displayed(), "Campo de senha não está presente"

# Passo 3: Inserir as credenciais corretas e clicar no botão de login
driver.find_element(By.ID, "email").send_keys("email@acordelab.com.br")
driver.find_element(By.ID, "senha").send_keys("123senha")
driver.find_element(By.CSS_SELECTOR, ".botao-login").click()

# Aguarda o redirecionamento para a página inicial
time.sleep(2)
assert "home.html" in driver.current_url, "O redirecionamento para a página inicial falhou após o login com credenciais válidas"

# Passo 5: Voltar à página de login e testar com credenciais incorretas
driver.get("https://almsantana.github.io/")  # Recarrega a página de login

# Passo 6: Inserir credenciais incorretas e verificar a mensagem de erro
driver.find_element(By.ID, "email").send_keys("errado@acordelab.com.br")
driver.find_element(By.ID, "senha").send_keys("senhaerrada")
driver.find_element(By.CSS_SELECTOR, ".botao-login").click()

# Verifica se a mensagem de erro "E-mail ou senha incorretos. Tente novamente." é exibida
mensagem_erro = driver.find_element(By.CSS_SELECTOR, ".mensagem-erro").is_displayed()
assert mensagem_erro, "A mensagem de erro não foi exibida após tentativa de login com credenciais inválidas"

# Aguarda 3 segundos antes de fechar o navegador
time.sleep(3)

# Fecha o navegador
driver.quit()