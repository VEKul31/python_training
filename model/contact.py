from sys import maxsize


class Contact:
    def __init__(self, name=None, middlename=None, lastname=None, id=None, address=None,
                 all_emails_from_home_page=None, email=None, email2=None, email3=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 all_phones_from_home_page=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.id = id
        self.address = address
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
#       self.group = group

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id)
                and self.name == other.name and self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
