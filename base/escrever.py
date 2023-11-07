from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
driver.get('https://cursoautomacao.netlify.app/desafios.html')

sleep(1)

# Para escrever usamos o comando send.keys()

email = driver.find_element(By.ID,"email") # achando botão
email.send_keys("npohsner@gmail.com") # escrevendo
sleep(1)
senha = driver.find_element(By.ID,"senha") # achando botão
senha.send_keys("123456") # escrevendo
sleep(1)
enviar = driver.find_element(By.CLASS_NAME,"btn.btn-primary") # achando botão
enviar.click() # clicando no botão

input('')
driver.close()