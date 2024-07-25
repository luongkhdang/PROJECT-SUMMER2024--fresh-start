from selenium import webdriver


def launchBrowser():
    browser = webdriver.Chrome()
    browser.get("https://github.com")

    signin_link = browser.find_element("link text", "Sign in")
    signin_link.click()

    username_box = browser.find_element("link text", "login_field")
    username_box.send_keys("adminid")
    password_box = browser.find_element("link text", "password")
    password_box.send_keys("adminpass")

    while (True):
        pass


launchBrowser()
