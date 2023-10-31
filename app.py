from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
# Inicializando Webdriver
driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
# Navegando até um site
driver.get("https://youtube.com")
# Necessario fazer algo, caso contrario ele executa e fecha
input("Aperte uma tecla para fechar.")
