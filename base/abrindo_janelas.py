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
# Salvar janela atual numa variavel
janela_atual = driver.current_window_handle
# Entrar na nova janela
driver.execute_script("window.scrollTo(0,500)")
sleep(2)
nova_janela = driver.find_element(By.XPATH,"//button[@class='btn btn-success']")
nova_janela.click()
sleep(2)
janelas = driver.window_handles
for janela in janelas:
    if janela not in janela_atual:
        driver.switch_to.window(janela)
        pesquisa = driver.find_element(By.XPATH,"//input[@id='campo_pesquisa']")
        pesquisa.send_keys("computador")   
        sleep(1)
        enter = driver.find_element(By.XPATH,"//button[@id='fazer_pesquisa']")
        enter.click()
        sleep(1)
        driver.close()
driver.switch_to.window(janela_atual)


input('')
driver.close()