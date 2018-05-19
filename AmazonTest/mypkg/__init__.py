from selenium import webdriver

DRIVER = None

def CreateWebdriver():
    global DRIVER

    DRIVER = DRIVER or webdriver.Firefox()
    return DRIVER



