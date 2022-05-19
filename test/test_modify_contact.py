
from model.contact import Contact

def test_modify_contact_name(app):
    if app.manager_contact.count() == 0:
        app.manager_contact.create(Contact(firstname="test"))
    old_contacts = app.manager_contact.get_contact_list()
    contact = Contact(firstname="New name")
    contact.id = old_contacts[0].id
    app.manager_contact.modify_first_contact_name(contact)
    new_contacts = app.manager_contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
