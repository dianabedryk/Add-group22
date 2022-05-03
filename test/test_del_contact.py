
def test_del_contact(app):
    app.manager.login(username="admin", password="secret")
    app.manager.delete_first_contact()
    app.manager.logout()