from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
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
driver.execute_script("window.scrollTo(0,1500)")
sleep(1)

# varias imagens numa mesma classe

imagens = driver.find_elements(By.XPATH,"//img[@class='img-thumbnail']")
cont = 1
for imagem in imagens:
    with open(f"imagem{cont}.png","wb") as arquivo:
        arquivo.write(imagem.screenshot_as_png)
        sleep(1)
    cont += 1

# uma imagem, vou pegar um site diferente

driver.get('https://pt.wikipedia.org/wiki/Brasil')
driver.maximize_window()
sleep(1)
bandeira = driver.find_element(By.XPATH,"//img[@alt='Bandeira do Brasil']")
sleep(1)
with open("bandeira.jpg","wb") as arquivo:
    arquivo.write(bandeira.screenshot_as_png)

input('')
driver.close()