from selenium import webdriver


def before_all(context):
    # create a Chrome webdriver instance
    driver = webdriver.Chrome()

    # set the context.driver to the created instance
    context.driver = driver
