from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

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
driver.get('https://cursoautomacao.netlify.app/')
driver.maximize_window()
sleep(1)

# Situação 1 - digitar o nome e clicar em alerta, fechar alerta.
driver.execute_script("window.scrollTo(0,250)")
nome_alerta = driver.find_element(By.ID,"nome")
sleep(2)
nome_alerta.send_keys("Newton")
sleep(2)
botao_alerta = driver.find_element(By.ID,"buttonalerta")
botao_alerta.click()
sleep(2)
alerta = driver.switch_to.alert
alerta.accept()

# Situação 2 - confirmar e dar ok
nome_alerta = driver.find_element(By.ID,"nome")
sleep(2)
nome_alerta.send_keys("Newton")
sleep(2)
botao_confirmar = driver.find_element(By.ID,"buttonconfirmar")
botao_confirmar.click()
sleep(2)
alerta2 = driver.switch_to.alert
# Confirmar
#alerta2.accept()
# Cancelar
alerta2.dismiss()

# Situação 3 - fazer pergunta

botao_pergunta = driver.find_element(By.ID,"botaoPrompt")
botao_pergunta.click()
sleep(2)
alerta3 = driver.switch_to.alert
sleep(2)
alerta3.send_keys("Sexta-Feira")
sleep(2)
alerta3.accept()
sleep(1)
alerta3.dismiss()





input('')
driver.close()