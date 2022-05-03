
from fixture.manager_group import Manager_groupHelper
from fixture.manager_contact import Manager_contactHelper


class DeleteHelper:

    def __init__(self, app):
        self.app = app
        self.manager_group = Manager_groupHelper(self)
        self.manager_contact = Manager_contactHelper(self)