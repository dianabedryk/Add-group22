
from model.group import Group



def test_add_group(app):
    app.manager_group.create(Group(name="gfuy", header="ihhn", footer="fgh"))

def test_add_empty_group(app):
    app.manager_group.create(Group(name="", header="", footer=""))

