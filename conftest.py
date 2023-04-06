import pytest
from selene import browser, have, be

@pytest.fixture()
def discovery():
    browser.open('https://www.google.com')


@pytest.fixture()
def to_expand(discovery):
    browser.driver.set_window_size(1920, 1080)
    yield
    browser.driver.set_window_size(800, 600)
