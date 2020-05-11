from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstagramBot():
    def __init__(self, username, password):
        """Inicialização dos atributos."""
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'geckodriver.exe')

    def login(self):
        """Inicia o Firefox."""
        driver = self.driver
        driver.get('https://www.instagram.com')
        sleep(3)

        # Identifica o user_name, limpa o campo e preenche com o nome de usuário.
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        sleep(1)
        user_element.send_keys(self.username)

        # Identifica o campo senha, limpa e preenche com a senha.
        pass_element = driver.find_element_by_xpath("//input[@name='password']")
        pass_element.clear()
        sleep(1)
        pass_element.send_keys(self.password)
        pass_element.send_keys(Keys.RETURN)
        sleep(5)

        # Encontrar o perfil e curtir a primeira foto.
        self.localizar_e_cutir('gustavoguanabara')

    def localizar_e_cutir(self, perfil):
        driver = self.driver
        driver.get('https://www.instagram.com/' + perfil + '/')
        sleep(1)

        # Clica na primeira foto.
        pic = driver.find_element_by_class_name("_9AhH0")
        pic.click()
        sleep(2)

        # Curti a primeira foto.
        like = driver.find_element_by_class_name('//button[@class="wpO6b "]') 
        sleep(2) 
        like.click()

instancia = InstagramBot('fratel.l', 'Le@nd42453390')
instancia.login()
# gustavoguanabara
# theaigirl