from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstagramBot:
    def __init(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        #//input[@name='username']
        #//input[@name='passwrd']

instancia = InstagramBot('heraklless', 'Le@nd42453390')
instancia.login()