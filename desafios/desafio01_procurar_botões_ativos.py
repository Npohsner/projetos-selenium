from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    return driver

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/desafios.html')

botao01 = driver.find_element(By.ID,"btn1")
if botao01.is_enabled():
    print("Botão 1 está Habilitado")
else:
    print("Botão 1 está Desabilitado")

botao02 = driver.find_element(By.CLASS_NAME,"btn2.btn.btn-dark")
if botao02.is_enabled():
    print("Botão 2 está Habilitado")
else:
    print("Botão 2 está Desabilitado")

botao03 = driver.find_element(By.CLASS_NAME,"btn2.btn.btn-warning")
if botao03.is_enabled():
    print("Botão 3 está Habilitado")
else:
    print("Botão 3 está Desabilitado")

input('')
driver.close()