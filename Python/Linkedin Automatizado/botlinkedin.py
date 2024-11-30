from random import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util import wait

# Entrando no site
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/feed/')
sleep(3)
options = webdriver.ChromeOptions()
options.add_argument("--disabled-gpu")

# Fazendo login
campo_usuario = driver.find_element(By.XPATH, "//input[@id='username']")
sleep(1)
campo_usuario.click()
usuario = str(input('Qual o seu usuário: '))
for l1 in usuario:
    campo_usuario.send_keys(l1)
    sleep(0.2)
campo_senha = driver.find_element(By.XPATH, "//input[@id='password']")
sleep(1)
campo_senha.click()
senha = str(input('Qual a sua senha: '))
for l2 in senha:
    campo_senha.send_keys(l2)
    sleep(0.1)
sleep(1)
botao_entrar = driver.find_element(By.XPATH, "//button[@class='btn__primary--large from__button--floating']")
botao_entrar.click()
sleep(10)

# Buscando
campo_busca = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
campo_busca.click()
profissao = str(input('Qual profissão deseja buscar: '))
campo_busca.send_keys(profissao)
sleep(1)
pyautogui.press('Enter')
sleep(3)
driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[2]/button').click()

# Conectando com pessoas


def conectarpessoas():
    conexoes_diarias = 0
    botaoconectar = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//button[span[text()="Conectar"]]'))
    )
    while True:
        try:
            botaoconectar = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//button[span[text()="Conectar"]]'))
            )

            for i in range(len(botaoconectar)):
                # Recarregar os elementos para evitar referência inválida
                botaoconectar = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//button[span[text()="Conectar"]]'))
                )
                botao = botaoconectar[i]

                try:
                    botao.click()
                    sleep(1)  # Pausa para transição

                    # Esperar o botão "Enviar sem nota" aparecer e clicar
                    botaoenviar = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[text()[normalize-space()="Enviar sem nota"]]'))
                    )
                    botaoenviar.click()
                    conexoes_diarias += 1
                    if conexoes_diarias == 20:
                        break
                    sleep(1)

                except Exception as e:
                    print(f"Erro ao interagir com o botão 'Enviar sem nota': {e}")
                    continue

        except Exception as e:
            print(f"Erro ao interagir com os botões 'Conectar': {e}")
            break


conectarpessoas()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
botao_pagina_2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '(//button[span[text()="2"]])[1]'))
)
botao_pagina_2.click()
conectarpessoas()
