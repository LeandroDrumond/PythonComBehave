from selenium.webdriver.common.by import By
import time

class PaginaPrincipal():
    def __init__(self, browser):
        self.browser = browser

    btn_avatar = (By.CSS_SELECTOR, "div.toolbar__user-picture > button.avatar-button")
    btn_entrar = (By.XPATH, "(//button[@id='login-button-Entrar'])[2]")
    iframe = (By.XPATH, "//div[@class='login-modal']/iframe")

    def click_avatar(self):
        return self.browser.find_element(*self.btn_avatar).click()
        time.sleep(2)

    def click_btnEntrar(self):
        return self.browser.find_element(*self.btn_entrar).click()

    def altera_iframe(self):
        return self.browser.switch_to.frame(self.browser.find_element(*self.iframe))

