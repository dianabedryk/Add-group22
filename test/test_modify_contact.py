
from model.contact import Contact

def test_modify_contact_name(app):
    app.manager_contact.login(username="admin", password="secret")
    app.manager_contact.modify_first_contact_name(Contact(firstname="New name"))
    app.manager_contact.logout()