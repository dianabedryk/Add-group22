
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class Manager_contactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new()
        self.fill_contact_form(contact)
        self.submit_add_address_book_entry()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_firstname_value("firstname", contact.firstname)
        self.change_firstname_value("middlename", contact.middlename)
        self.change_lastname_value("lastname", contact.lastname)
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


    def change_firstname_value(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)

    def change_lastname_value(self, field_lastname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_lastname).click()
            wd.find_element_by_name(field_lastname).clear()
            wd.find_element_by_name(field_lastname).send_keys(text)


    def change_day_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def submit_add_address_book_entry(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select first group
        self.select_contact_by_index(index)
        # submit deletion
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact_name(self):
        self.modify_contact_by_index(0)


    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_modification_form_by_index(index)
        self.fill_contact_form(new_contact_data)
        self.submit_modification()
        self.app.return_to_home_page()
        self.contact_cache = None

    def open_modification_form_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_modification_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def submit_modification(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None



    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            row = wd.find_elements_by_xpath("//tr[position() >1]")
            for element in row:
                id = element.find_element_by_xpath(".//td/input[@type='checkbox']").get_attribute("value")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                all_phones = element.find_element_by_xpath(".//td[6]").text

                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//tbody/tr/td[7]")[index].click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        firstname = wd.find_element_by_name("firstname:").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                       home_phone=home_phone, work_phone=work_phone, mobile_phone=mobile_phone)





