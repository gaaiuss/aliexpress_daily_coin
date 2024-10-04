from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configurações do Edge (opcionalmente pode adicionar argumentos)
edge_options = Options()
# edge_options.add_argument("--headless")  # Se você quiser rodar em modo headless

# Caminho para o msedgedriver baixado
service = Service(executable_path='C:\\Users\\caiog\\Downloads\\edgedriver_win64\\msedgedriver.exe')

# Inicializar o driver do Edge
driver = webdriver.Edge(service=service, options=edge_options)

# Acessar uma página de exemplo
driver.get('https://www.aliexpress.com')
time.sleep(2)

# Fazer login (você pode precisar ajustar dependendo do método de login)
close_popup_button = driver.find_element(By.CLASS_NAME, 'pop-close-btn')
close_popup_button.click()
time.sleep(1)

dropdown = driver.find_element(By.CLASS_NAME, 'my-account--menuItem--1GDZChA')
# Criar uma instância de ActionChains
actions = ActionChains(driver)
# Mover o mouse para o dropdown
actions.move_to_element(dropdown).perform()
time.sleep(2)

login_bt = driver.find_element(By.CLASS_NAME, 'my-account--signin--RiPQVPB')
login_bt.click()
time.sleep(2)

# # Preencher credenciais de login (se necessário)
# email_field = driver.find_element(By.NAME, 'email')
# email_field.send_keys('seu_email')
# password_field = driver.find_element(By.NAME, 'password')
# password_field.send_keys('sua_senha')
# password_field.send_keys(Keys.RETURN)
# time.sleep(5)  # Esperar tempo suficiente para o login ser processado

# # Navegar até a página de resgate de moedas
# driver.get('https://www.aliexpress.com/p/coin-pc-index/index.html?spm=a2g0o.best.headerAcount.3.f23a22ae4DhcLS')  # Precisa descobrir a URL específica para resgate de moedas

# # Encontrar e clicar no botão de resgatar moedas
# collect_button = driver.find_element(By.CLASS_NAME, 'checkin-button')  # Nome da classe fictício, ajusta conforme a página
# collect_button.click()

# Fechar o navegador após completar
# time.sleep(2)
input()
driver.quit()