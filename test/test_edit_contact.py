from model.contact import Edit_contact


def test_edit_first_contact(app):
    app.manager_contact.edit_first_contact(Edit_contact(first_name="ddd", middle_name="dddd", last_name="ddd", nickname="dddd", address="dddd",
                                           home_phone="dddd", mobil_phone="dddd", email2="dddd", address2="dddd"))
