# -*- coding: utf-8 -*-
import pytest
from Model.contact import Contact
from fixture.application1 import Application1


@pytest.fixture
def app(request):
    fixture = Application1()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.fill_add_address_book_entry(Contact(firstname="dfg", middlename="kmn", lastname="yhj", nickname="rgi",
                                         title="olk", company="tyj", address="iolkn", home_phone="tyhk", mobile_phone="fgbnm",
                                         work_phone="rtjl", fax="vgythk", email="tyjkm", email2="tyhbnmk", email3="yujkl,",
                                         homepage="tyhklm", bday="15", bmonth="March", byear="1980", aday="14",
                                         amonth="August", ayear="2010", address2="thjmb", home_phone2="tyjmn",
                                         notes="cvbnyt"))
    app.logout()


def test_add_empty_contact(app):
        app.login(username="admin", password="secret")
        app.fill_add_address_book_entry(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                                             company="", address="", home_phone="", mobile_phone="", work_phone="",
                                             fax="", email="", email2="", email3="",
                                             homepage="", bday="", bmonth="-", byear="", aday="",
                                             amonth="-", ayear="", address2="", home_phone2="",
                                             notes=""))
        app.logout()

