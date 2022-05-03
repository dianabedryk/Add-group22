from fixture.manager import ManagerHelper


class SessionHelper:

    def __init__(self, app):
        self.app = app
        self.manager = ManagerHelper(self)







