
def test_delete_first_contact(app):
    app.manager_contact.login(username="admin", password="secret")
    app.manager_contact.delete_first_contact()
    app.manager_contact.logout()