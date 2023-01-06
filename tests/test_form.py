from demoqa_test.model.pages import practise_form


def test_form_registration():
    practise_form.open_registration_form()

    # WHEN
    practise_form.type_firstname('Sergey')
    practise_form.type_lastname('QA')
    practise_form.type_email('pochta@example.com')
    practise_form.select_gender('Male')
    practise_form.type_phone_number('8800553555')
    practise_form.click_databirthday()
    practise_form.select_month('July')
    practise_form.select_year('1999')
    practise_form.select_day('08')
    practise_form.type_subject('Math')
    practise_form.select_hobby('Sports')
    practise_form.upload_picture('picture/stich.jpg')
    practise_form.type_address('street Pushkina, home 5')
    practise_form.select_state('NCR')
    practise_form.select_city('Delhi')
    practise_form.submit()

    # THEN
    practise_form.check_results(
        'Sergey QA',
        'pochta@example.com',
        'Male',
        '8800553555',
        '08 July,1999',
        'Maths',
        'Sports',
        'stich.jpg',
        'street Pushkina, home 5',
        'NCR Delhi'
    )