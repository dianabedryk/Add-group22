from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.manager_contact import Manager_contactHelper
from fixture.manager_group import Manager_groupHelper



class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.manager_contact = Manager_contactHelper(self)
        self.manager_group = Manager_groupHelper(self)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()