from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
arguments = ["--lang=pt-BR","--window-size=800,800","--incognito"]
for argument in arguments:
    chrome_options.add_argument(argument)
# Uso de conficurações Experimentais
chrome_options.add_experimental_option('prefs', {
    # Alterar local padrão de download de arquivos
    'dowload.default_directory': 'C:\\Users\\Nextpc\\Desktop\\CURSO MESTRE DA AUTOMAÇÃO\\projetos-selenium\\downloads',
    # Notificar google chrome sobre a alteração
    'download.directory_upgrade': True,
    # Desabilitar confirmação de Download
    'download.prompt_for_download': False,
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications': 2,
    # Permitir multiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,
})

 
# Inicializando Webdriver
driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()),options=chrome_options)
# Navegando até um site
driver.get("https://pt.wikipedia.org/wiki/Brasil")
# Necessario fazer algo, caso contrario ele executa e fecha
input("Aperte uma tecla para fechar.")
