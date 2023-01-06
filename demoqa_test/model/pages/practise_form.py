from selene.support.conditions import have
from selene.support.shared import browser
from demoqa_test.model.control import checkboxs, datapiecker, dropdown, radio_button
from demoqa_test.utils import upload


def open_registration_form():
    browser.open('/automation-practice-form')


def type_firstname(text):
    browser.element('#firstName').type(text)


def type_lastname(text):
    browser.element('#lastName').type(text)


def type_email(email):
    browser.element('#userEmail').type(email)


def select_gender(value):
    radio_button.gender(browser.all('[for="gender-radio-1"'), value)


def type_phone_number(number):
    browser.element('#userNumber').type(number)


def click_databirthday():
    browser.element('#dateOfBirthInput').click()


def select_month(value):
    browser.element('.react-datepicker__month-select').click()
    datapiecker.data_birthday('.react-datepicker__month-select', value)


def select_year(value):
    browser.element('.react-datepicker__year-select').click()
    datapiecker.data_birthday('.react-datepicker__year-select', value)


def select_day(value):
    browser.element(f'.react-datepicker__day--0{value}').click()


def type_subject(text):
    browser.element('#subjectsInput').type(text).press_enter()


def select_hobby(value):
    checkboxs.hobby('[for^="hobbies-checkbox"]', value)


def upload_picture(path):
    upload.path_picture('#uploadPicture', path)


def select_state(text):
    dropdown.select('#state', text)


def select_city(text):
    dropdown.select('#city', text)


def type_address(text):
    browser.element('#currentAddress').type(text)


def submit():
    browser.element('#submit').click()


def check_results(texts):
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(texts))