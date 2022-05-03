
def test_delete_first_group(app):
    app.manager_group.login(username="admin", password="secret")
    app.manager_group.delete_first_group()
    app.manager_group.logout()