
class Contact:
    def __init__(self, name=None, middlename=None, lastname=None, email=None, id=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.email = email
        self.id = id
        #self.group = group

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

