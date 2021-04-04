# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:17:13 2021

@author: Z440
"""
import time


def test_check_add_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(5)
    time.sleep(10)
    add_key = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert add_key.is_displayed() == True, "the button not find"
    browser.quit()
