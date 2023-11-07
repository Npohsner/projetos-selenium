from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random



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

def digitacao_humanizada(texto,elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1,3)/30)


driver.get('https://cursoautomacao.netlify.app/desafios.html')
driver.maximize_window()
sleep(1)

texto = ("A mais bela experiência que podemos ter é o mistério. É a emoção fundamental que está no berço da verdadeira arte e da verdadeira ciência “. “Uma pessoa que nunca cometeu um erro, nunca tentou nada novo.")

paragrafo = driver.find_element(By.ID,"campoparagrafo")
digitacao_humanizada(texto,paragrafo)

input('')
driver.close()