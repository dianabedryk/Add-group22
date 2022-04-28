from selenium import webdriver
from fixture.session import Session_contactHelper
from fixture.group import Group_contactHelper
from fixture.manager import Manager_contactHelper

class Application1:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_contact = Session_contactHelper(self)
        self.group_contact = Group_contactHelper(self)
        self.manager_contact = Manager_contactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()