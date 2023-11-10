from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
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
driver.get('https://cursoautomacao.netlify.app/exemplo_chains')
driver.maximize_window()
sleep(1)
# Achar o botão
clique_aqui = driver.find_element(By.ID,"botao-direito")
# Inicializar o ActionChains
chain = ActionChains(driver)
# Simular click com botão direito, escolher opção usando DOWN do teclado, clicar na opção desejada.
chain.context_click(clique_aqui).pause(1).send_keys(Keys.DOWN).pause(1).send_keys(Keys.DOWN).pause(1).send_keys(Keys.DOWN).pause(1).click().perform()


input('')
driver.close()