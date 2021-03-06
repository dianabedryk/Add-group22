

from model.contact import Contact



def test_add_contact(app):
    old_contacts = app.manager_contact.get_contact_list()
    contact = Contact(firstname="dfg", middlename="kmn", lastname="yhj", nickname="rgi",
            title="olk", company="tyj", address="iolkn", home_phone="2142018446", mobile_phone="2142038446",
            work_phone="2162138664", fax="vgythk", email="tyjkm", email2="tyhbnmk", email3="yujkl,",
            homepage="tyhklm", bday="15", bmonth="March", byear="1980", aday="14",
            amonth="August", ayear="2010", address2="thjmb", home_phone2="2152368559",
            notes="cvbnyt")
    app.manager_contact.create(contact)
    assert len(old_contacts) + 1 == app.manager_contact.count()
    new_contacts = app.manager_contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_add_empty_contact(app):
#   old_contacts = app.manager_contact.get_contact_list()
#    app.manager_contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="",
#                                       company="", address="", home_phone="", mobile_phone="", work_phone="",
#                                       fax="", email="", email2="", email3="",
#                                       homepage="", bday="", bmonth="-", byear="", aday="",
#                                       amonth="-", ayear="", address2="", home_phone2="",
#                                       notes=""))
#    new_contacts = app.manager_contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)