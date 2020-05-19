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
        self.localizar('ambsiau')

    def localizar(self, perfil):
        driver = self.driver
        driver.get('https://www.instagram.com/' + perfil + '/')
        sleep(3)

        # Clica na primeira foto.
        pic = driver.find_element_by_class_name("_9AhH0")

        # Localiza o botão de like.
        like = driver.find_element_by_class_name("fr66n")

        # passa para a proxima foto.
        prx_foto = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')

        pic.click()
        # Executa o loop para curtir todas as fotos do perfil.
        while pic == True:
            sleep(4)
            like.click()
            sleep(4)
            prx_foto.click()

instancia = InstagramBot('heraklless', 'Le@nd42453390')
instancia.login()

# gustavoguanabara
# ambsiau