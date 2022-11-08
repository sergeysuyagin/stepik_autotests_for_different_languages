from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_cart_button_is_on_page(browser):
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        element_is_on_page = True
    except:
        element_is_on_page = False
    assert element_is_on_page, "Add to cart button not found"
