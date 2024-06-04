
from browser import Browser
from pages.login_page import LoginPage


def before_all(context):
    """
    Vom defini toate instructiunile care trebuie executate
    inaintea rularii tuturor pasilor
    """
    context.browser = Browser()
    context.login_page = LoginPage()


def after_all(context):
    """
    Vom defini toate instructiunile care trebuie executate
    dupa rularea tuturor pasilor
    """
    context.browser.close()
