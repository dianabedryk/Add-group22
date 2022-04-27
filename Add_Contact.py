# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact
from aplication1 import Application1

class AddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application1()

    def test_add_contact(self):
        self.login(username="admin", password="secret")
        self.fill_add_address_book_entry(Contact(firstname="dfg", middlename="kmn", lastname="yhj", nickname="rgi",
                                         title="olk", company="tyj", address="iolkn", home_phone="tyhk", mobile_phone="fgbnm",
                                         work_phone="rtjl", fax="vgythk", email="tyjkm", email2="tyhbnmk", email3="yujkl,",
                                         homepage="tyhklm", bday="15", bmonth="March", byear="1980", aday="14",
                                         amonth="August", ayear="2010", address2="thjmb", home_phone2="tyjmn",
                                         notes="cvbnyt"))
        self.logout()

    def test_add_empty_contact(self):
            self.login(username="admin", password="secret")
            self.fill_add_address_book_entry(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                                             company="", address="", home_phone="", mobile_phone="", work_phone="",
                                             fax="", email="", email2="", email3="",
                                             homepage="", bday="", bmonth="-", byear="", aday="",
                                             amonth="-", ayear="", address2="", home_phone2="",
                                             notes=""))
            self.logout()



    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
