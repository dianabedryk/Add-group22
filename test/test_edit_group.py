from model.group import Edit_group

def test_add_group(app):
    app.manager.login(username="admin", password="secret")
    app.manager.edit_first_group(Edit_group(name="a", header="aa", footer="aaa"))
    app.manager.logout()