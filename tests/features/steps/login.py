from behave import given, when, then
from tests.page_objects import *
from selenium.webdriver import Chrome
import time

@given(u'que usuário possa acessar a tela de login do sistema')
def step_acessa_pagina_login(context):
    paginaPrincipal = PaginaPrincipal(context.browser)
    paginaPrincipal.click_avatar()
    paginaPrincipal.click_btnEntrar()
    paginaPrincipal.altera_iframe()

@when(u'inserir um email valido')
def step_informa_emailValido(context):
   email = context.config.userdata.get('email')
   paginaLogin = LoginPage(context.browser)
   paginaLogin.click_formEmail()
   paginaLogin.limpa_form()
   paginaLogin.digita_email(email)

@when(u'inserir uma senha válida e clicar em Entrar')
def step_informa_senhaValida(context):
    senha = context.config.userdata.get('senha')
    paginaLogin = LoginPage(context.browser)
    paginaLogin.click_formSenha()
    paginaLogin.digita_senha(senha)
    paginaLogin.click_btnEntrar()


@then(u'o nome do usuario logado deve ser exibido.')
def step_impl(context):
    paginaLogada = PaginaLogada(context.browser)
    paginaLogada.alteraFocopaginaPrincipal()
    esperaPadrao = int(context.config.userdata.get('esperaPadrao'))
    time.sleep(esperaPadrao)
    paginaLogada.click_avatar()
    time.sleep(esperaPadrao)
    paginaLogada.validaUserLogado()
