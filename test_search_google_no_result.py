import pytest
from selene import browser, have, be
def test_no_result(discovery,to_expand):
    browser.element('[name="q"]').type('58946456446454').press_enter()
    browser.element('[id="topstuff"]').should(have.text('По запросу 58946456446454 ничего не найдено.'))