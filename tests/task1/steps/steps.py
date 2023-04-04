from behave import given, when, then

from page_objects.main_page import MainPage


@given('I open main page')
def open_main_page(context):
    print("Navigating to the main page...")
    main_page = MainPage(context.driver)
    main_page.open()
