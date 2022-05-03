
from model.group import Edit_group

def test_add_group(app):
    app.manager_group.login(username="admin", password="secret")
    app.manager_group.edit_first_group(Edit_group(name="a", header="aa", footer="aaa"))
    app.manager_group.logout()