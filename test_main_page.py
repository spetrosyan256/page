from selenium.webdriver.common.by import By
import time
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_linok")
    login_link.click()