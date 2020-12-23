import time

def test_check_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = None
    button = browser.find_element_by_css_selector("button.btn")
    assert button != None, "Кнопка отсутствует!"