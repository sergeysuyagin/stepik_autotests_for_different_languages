from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_cart_button_is_on_page(browser):
    browser.get(link)
    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(buttons) > 0, "Add to cart button not found"
