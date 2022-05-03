
from model.group import Group



def test_add_group(app):
    app.manager_group.login(username="admin", password="secret")
    app.manager_group.create(Group(name="gfuy", header="ihhn", footer="fgh"))
    app.manager_group.logout()

def test_add_empty_group(app):
    app.manager_group.login(username="admin", password="secret")
    app.manager_group.create(Group(name="", header="", footer=""))
    app.manager_group.logout()

