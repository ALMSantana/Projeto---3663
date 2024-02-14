from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Configurando o driver do Selenium
selenium_service = Service('driver/chromedriver.exe')
driver = webdriver.Chrome(service=selenium_service)

# Abrindo o aplicativo AcordeLab
driver.get('https://almsantana.github.io/')

time.sleep(3)

# Localizando o campo de login na tela inicial
login_field = driver.find_element(By.ID, 'email')

# Inserindo o nome de usuário
login_field.send_keys('email@acordelab.com.br')

# Inserindo a senha
password_field = driver.find_element(By.ID, 'senha')
password_field.send_keys('123senha')

# Clicando no botão "Entrar"
login_button = driver.find_element(By.CLASS_NAME, 'botao-login')
login_button.click()

# Pausa de 3 segundos antes de fechar o script
time.sleep(3)

# Fechando o script
driver.quit()
