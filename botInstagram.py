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
        sleep(2)

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
        sleep(7)

        # Encontrar o perfil e curtir a primeira foto.
        self.localizar_e_cutir('gustavoguanabara')

    def localizar_e_cutir(self, perfil):
        driver = self.driver
        driver.get('https://www.instagram.com/' + perfil + '/')
        sleep(2)

        # Clica na primeira foto.
        pic = driver.find_element_by_class_name("_9AhH0")
        pic.click()
        sleep(3)
        
        # Curtir
        like = driver.find_element_by_class_name("fr66n")
        like.click()
        sleep(3)

        # Proxima foto.
        prx_foto = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
        prx_foto.click()
        sleep(3)

        while True:
            b_like = driver.find_element_by_class_name("fr66n").click()
            prx_foto.click()
            sleep(7)
      

instancia = InstagramBot('fratel.', 'Le@nd42453390')
instancia.login()

# celia_gabbiani44
# jas_stayfit
# gustavoguanabara