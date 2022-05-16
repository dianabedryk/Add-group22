# -*- coding: utf-8 -*-

from model.contact import Contact



def test_add_contact(app):
    app.manager_contact.create(Contact(firstname="dfg", middlename="kmn", lastname="yhj", nickname="rgi",
                                       title="olk", company="tyj", address="iolkn", home_phone="tyhk", mobile_phone="fgbnm",
                                       work_phone="rtjl", fax="vgythk", email="tyjkm", email2="tyhbnmk", email3="yujkl,",
                                       homepage="tyhklm", bday="15", bmonth="March", byear="1980", aday="14",
                                       amonth="August", ayear="2010", address2="thjmb", home_phone2="tyjmn",
                                       notes="cvbnyt"))

def test_add_empty_contact(app):
    app.manager_contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                                       company="", address="", home_phone="", mobile_phone="", work_phone="",
                                       fax="", email="", email2="", email3="",
                                       homepage="", bday="", bmonth="-", byear="", aday="",
                                       amonth="-", ayear="", address2="", home_phone2="",
                                       notes=""))