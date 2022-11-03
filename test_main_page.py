import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    # page.should_be_login_link()                           # проверка ссылки без перехода
    page.go_to_login_page()
    # login_page = page.go_to_login_page()                  # явный переход на страницу login
    login_page = LoginPage(browser, browser.current_url)    # неявный переход на страницу login
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()
#   this string for Git test
