
def test_delete_first_group(app):
    app.manager.login(username="admin", password="secret")
    app.manager.delete_first_group()
    app.manager.logout()