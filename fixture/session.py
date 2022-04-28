from fixture.manager import Manager_contactHelper
from fixture.manager import Manager_groupHelper

class Session_groupHelper:

    def __init__(self, app):
        self.app = app
        self.manager_group = Manager_groupHelper(self)


class Session_contactHelper:
    def __init__(self, app):
        self.app = app
        self.manager_contact = Manager_contactHelper(self)
