from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.manager_contact.count() == 0:
        app.manager_contact.create(Contact(firstname="test"))
    old_contacts = app.manager_contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.manager_contact.delete_contact_by_index(index)
    new_contacts = app.manager_contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
