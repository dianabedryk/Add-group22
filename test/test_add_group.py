
from model.group import Group



def test_add_group(app):
    app.manager.login(username="admin", password="secret")
    app.manager.create(Group(name="gfuy", header="ihhn", footer="fgh"))
    app.manager.logout()

def test_add_empty_group(app):
    app.manager.login(username="admin", password="secret")
    app.manager.create(Group(name="", header="", footer=""))
    app.manager.logout()

