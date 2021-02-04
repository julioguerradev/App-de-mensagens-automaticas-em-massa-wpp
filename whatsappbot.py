#0- importar as bibliotecas
from selenium import webdriver
import time
#_____Simular o uso do navegador sem ferramentas extras_____
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#1- Navegar até o Whats app web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
#2- Definir contatos/grupos e mensagem a ser enviada
contatos =['Bot Teste', 'Vida Lindaaaa', 'Bolota Vivo']
mensagem = 'Te Amooooo(Essa mensagem foi mandata por m bot, porém com o sentimento de quem o fez!)'
#Buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(1)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
#Campo de pesquisa 'copyable-text selectable-text'
#Campo de mensagem privada 'copyable-text selectable-text'
#Enviar mensagens para o contato/grupo
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(1)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)