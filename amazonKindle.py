#O projeto é acessar o site da Amazon, realizar a busca por um Kindle
#selenecionar um modelo, no caso será o primeiro que aparece no resultado, e após
#a abertura da tela do kindle selecionado adicionar o mesmo carrinho.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configura o driver do Chrome automaticamente usando o WebDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://www.amazon.com.br")

    # Localiza o campo de pesquisa e realiza a busca por "kindle"
    kindle = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    kindle.send_keys("kindle")
    kindle.send_keys(Keys.RETURN)

    # Aguarda a exibição dos resultados da busca
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

    # Clica no kindle escolhido
    kindle = driver.find_element(By.XPATH, "(//div[@data-component-type='s-search-result']//a[@class='a-link-normal s-no-outline'])")
    kindle.click()

    # Aguarda a página do kindle selecionado
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='add-to-cart-button']")))

    # Aós carregar a página adiciona o kindle ao carrinho
    add_carrinho = driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']")
    add_carrinho.click()

finally:
    # Fecha o navegador
    driver.quit()
