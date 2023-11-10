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
driver.get('https://cursoautomacao.netlify.app/desafios.html')
driver.maximize_window()
sleep(2)
# Salvar pagina atual
janela_inicial = driver.current_window_handle
# Rolar a pagina para o final dela
driver.execute_script("window.scrollTo(0,3000)")
sleep(2) 
# Abrini nova janela
nova_janela = driver.find_element(By.XPATH,"//button[@onclick='abrirJanelaDesafio()']")
nova_janela.click()
sleep(2)
# Alternar para a nova janela
janelas = driver.window_handles
for janela in janelas:
    if janela not in janela_inicial:
        driver.switch_to.window(janela)
# Achar novo campo escrever, enviar e fechar pagina
        novo_campo = driver.find_element(By.XPATH,"//textarea[@id='opiniao_sobre_curso']") 
        novo_campo.click()
        sleep(1)
        novo_campo.send_keys("Incrivel !!!")
        sleep(1)
        pesquisar = driver.find_element(By.XPATH,"//button[@id='fazer_pesquisa']")              
        pesquisar.click()
        sleep(1)
        driver.close()
# Alternar para a pagina inicialmente aberta
driver.switch_to.window(janela_inicial)
sleep(2)
# Deixando mensagem na pagina inicial
mensagem_final = driver.find_element(By.XPATH,"//textarea[@id='campo_desafio7']")
mensagem_final.send_keys("FIM DO DESAFIO!!!!")


input('')
driver.close()