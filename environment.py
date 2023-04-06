from selenium import webdriver


def before_all(context):
    # Create a webdriver instance (replace with your preferred browser)
    context.driver = webdriver.Chrome()


def after_all(context):
    # Quit the webdriver instance
    context.driver.quit()
