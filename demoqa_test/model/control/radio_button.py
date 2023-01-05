from selene.support.conditions import have
from selene.support.shared import browser


def gender(selector, value):
    browser.all(selector).element_by(have.text(value)).element('..').click()