from selenium import webdriver
from fixture.group import Group_contactHelper
from fixture.session import Session_contactHelper

class Application1:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.group_contact = Group_contactHelper(self)
        self.session_contact = Session_contactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()