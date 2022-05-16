
from model.contact import Contact

def test_modify_contact_name(app):
    if app.manager_contact.count() == 0:
        app.manager_contact.create(Contact(firstname="test"))
    app.manager_contact.modify_first_contact_name(Contact(firstname="New name"))
