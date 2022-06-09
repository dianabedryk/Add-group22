from model.contact import Contact
from random import randrange

def test_modify_contact_name(app):
    if app.manager_contact.count() == 0:
        app.manager_contact.create(Contact(firstname="test"))
    old_contacts = app.manager_contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New name", lastname="New lastname")
    contact.id = old_contacts[index].id
    app.manager_contact.modify_contact_by_index(index, contact)
    new_contacts = app.manager_contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
