
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Manager_contactHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()
        wd.find_element(by=By.NAME, value="user")

    def open_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_add_address_book_entry(self, contact):
        wd = self.app.wd
        self.open_add_new()
        self.fill_contact_form(contact)
        self.submit_add_address_book_entry()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_firstname_value("firstname", contact.firstname)
        self.change_firstname_value("middlename", contact.middlename)
        self.change_firstname_value("lastname", contact.lastname)
        self.change_firstname_value("nickname", contact.nickname)
        self.change_firstname_value("title", contact.title)
        self.change_firstname_value("company", contact.company)
        self.change_firstname_value("address", contact.address)
        self.change_firstname_value("home", contact.home_phone)
        self.change_firstname_value("mobile", contact.mobile_phone)
        self.change_firstname_value("work", contact.work_phone)
        self.change_firstname_value("fax", contact.fax)
        self.change_firstname_value("email", contact.email)
        self.change_firstname_value("email2", contact.email2)
        self.change_firstname_value("email3", contact.email3)
        self.change_firstname_value("homepage", contact.firstname)
        self.change_day_value("bday", contact.bday)
        self.change_day_value("bmonth", contact.bmonth)
        self.change_firstname_value("byear", contact.byear)
        self.change_day_value("aday", contact.aday)
        self.change_day_value("amonth", contact.amonth)
        self.change_firstname_value("ayear", contact.ayear)
        self.change_firstname_value("address2", contact.address2)
        self.change_firstname_value("phone2", contact.home_phone2)
        self.change_firstname_value("notes", contact.notes)


    def change_firstname_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def change_day_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def submit_add_address_book_entry(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def modify_first_contact_name(self, new_contact_data):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        self.open_modification_form()
        self.fill_contact_form(new_contact_data)
        self.submit_modification()


    def edit_first_contact(self, edit_contact):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        self.open_modification_form()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(edit_contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(edit_contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(edit_contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(edit_contact.nickname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(edit_contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(edit_contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(edit_contact.mobil_phone)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(edit_contact.email2)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(edit_contact.address2)
        self.submit_modification()

    def open_modification_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def submit_modification(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)



