
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home_phone=None,
                                    mobile_phone=None, work_phone=None, fax=None, email=None, email2=None, email3=None, homepage=None,
                                    bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None,
                                    address2=None, home_phone2=None, notes=None, id= None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.home_phone2 = home_phone2
        self.notes = notes
        self.id = id

class Edit_contact:
    def __init__(self, first_name, middle_name, last_name, nickname, address, home_phone, mobil_phone, email2,
                           address2, id= None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.address = address
        self.home_phone = home_phone
        self.mobil_phone = mobil_phone
        self.email2 = email2
        self.address2 = address2
        self.id = id

