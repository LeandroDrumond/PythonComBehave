from selenium.webdriver.common.by import By
import time

class PaginaLogada():

    btn_avatar = (By.CSS_SELECTOR, "div.toolbar__user-picture > button.avatar-button")
    nomeLogado = (By.XPATH, "/html/body/div[1]/div/div/div/header/div[2]/div[2]/div[2]/div/div[1]/div[1]")

    def __init__(self, browser):
        self.browser = browser

    def alteraFocopaginaPrincipal(self):
        return self.browser.switch_to.default_content()

    def click_avatar(self):
        return self.browser.find_element(*self.btn_avatar).click()
        time.sleep(2)

    def validaUserLogado (self,user):
        usuarioPagina = self.browser.find_element(*self.nomeLogado).text
        return assert usuarioPagina == user