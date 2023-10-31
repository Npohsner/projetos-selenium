from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
arguments = ["--lang=pt-BR","--window-size=800,800","--incognito"]
for argument in arguments:
    chrome_options.add_argument(argument)
# Uso de conficurações Experimentais
chrome_options.add_experimental_option("prefs",{
    # Alterar local padrão do arquivo
    "download.default.directory":"C:\\Users\\Nextpc\\Desktop\\CURSO MESTRE DA AUTOMAÇÃO\\projetos-selenium\\downloads"
    # Notificar o google chrome sobre ess alteração
    "download.directory_upgrade": ,
    # Desabilitar a confirmação de download
    "download.prompt_for_dowload": False,
    # Desabilitar notificações do navegador
    "profile.default._content_setting_values.notifications": 2,
    # Permitir multiplos downloads
    "profile.default._content_setting_values.automatic_downloads": 1,
}) 
# Inicializando Webdriver
driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()),options=chrome_options)
# Navegando até um site
driver.get("https://pt.wikipedia.org/wiki/Brasil")
# Necessario fazer algo, caso contrario ele executa e fecha
input("Aperte uma tecla para fechar.")
