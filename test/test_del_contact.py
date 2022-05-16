from model.contact import Contact

def test_delete_first_contact(app):
    if app.manager_contact.count() == 0:
        app.manager_contact.create(Contact(firstname="test"))
    app.manager_contact.delete_first_contact()