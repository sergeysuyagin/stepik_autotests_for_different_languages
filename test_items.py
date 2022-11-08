from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_to_cart_button(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button, 'Add to cart button not found'
    
