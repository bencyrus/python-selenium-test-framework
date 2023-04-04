from page_objects.main_page import MainPage


def assert_main_page_title(driver, expected_title):
    # Asserts that the main page title is correct.
    main_page = MainPage(driver)
    print(f"The main page title is: {main_page.get_title()}")
    print(f"The expected title is: {expected_title}")

    assert main_page.get_title() == expected_title, \
        f"Expected title '{expected_title}' but got {main_page.get_title()}"

    print("The main page title is as expected.")

def