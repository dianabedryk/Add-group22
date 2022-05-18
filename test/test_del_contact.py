from model.contact import Contact

def test_delete_first_contact(app):
    if app.manager_contact.count() == 0:
        app.manager_contact.create(Contact(firstname="test"))
    old_contact = app.manager_contact.get_contact_list()
    app.manager_contact.delete_first_contact()
    new_contact = app.manager_contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
