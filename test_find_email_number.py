import PhoneAndEmailScraper


def test_find_phones():
    assert '415-863-9900' == PhoneAndEmailScraper.findPhoneNumbers('415-863-9900')


def test_find_email():
    assert 'anzm@gmail.com' == PhoneAndEmailScraper.findEmail('anzm@gmail.com')
