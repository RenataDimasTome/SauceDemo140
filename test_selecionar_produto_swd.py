# 1 - Bibliotecas
# Snake_case = jeito de escrever, p/ que as palavras não fiquem juntas coloca o anderlaine  
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (Opcional)
class Test_Produtos():

    # 2,1 Atributos
    url = "https://www.saucedemo.com"            # endereço do site alvo

    # 2.2 Funções e Métodos
    def setup_method(self, method):              # método de iniciar os testes
        self.driver = webdriver.Chrome()           # instancia do objeto do selenium webdriver com  chrome
        self.driver.implicitly_wait(10)          # define o tempo de espera padrão por elementos em 10 segundos

    def teardown_method(self, method):               # método de finalização dos testes
        self.driver.quit()                        # encerra/destrói o objeto do selenium webdriver da memória

    def test_selecionar_produto(self):            # método de teste
        self.driver.get(self.url)                # abre o navegador 
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user") # escreve no campo user-name
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce") # escreve a senha 