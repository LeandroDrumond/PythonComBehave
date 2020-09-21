from selenium.webdriver.common.by import By
import time

class LoginPage():

    def __init__(self, browser):
        self.browser = browser

    form_email = (By.ID,'login')
    form_password = (By.ID,'password')
    btn_logar = (By.CSS_SELECTOR, "#login-form > div.actions > button")

    def click_formEmail(self):
        return self.browser.find_element(*self.form_email).click()
        time.sleep(2)

    def limpa_form(self):
        return self.browser.find_element(*self.form_email).clear()

    def digita_email(self,email):
         string = self.browser.find_element(*self.form_email)
         return string.send_keys(email)

    def click_formSenha(self):
         return self.browser.find_element(*self.form_password).click()

    def digita_senha(self,senha):
          return self.browser.find_element(*self.form_password).send_keys(senha)

    def click_btnEntrar(self):
         return self.browser.find_element(*self.btn_logar).click()