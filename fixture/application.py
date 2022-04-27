from selenium import webdriver
from fixture.session import Session_groupHelper
from fixture.group import Group_groupHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_group = Session_groupHelper(self)
        self.group_group = Group_groupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()