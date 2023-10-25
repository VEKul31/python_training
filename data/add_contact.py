import random
import string
from model.contact import Contact


constant = [
    Contact(name="name1", lastname="lastname1",
            address="123", email="123", mobilephone="123"),
    Contact(name="name2", lastname="lastname2",
            address="234", email="234", mobilephone="234")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = ([Contact(name="", lastname="",
                     address="", email="", email2="", email3="",
                     homephone="", mobilephone="", workphone="", secondaryphone="")] +
            [
                Contact(name=random_string("name", 10), lastname=random_string("lastname", 10),
                        address=random_string("address", 10), email=random_string("email", 10),
                        mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10))
                for i in range(2)
            ])

testdata2 = [
    Contact(name=name, lastname=lastname, address=address, email=email, mobilephone=mobilephone, workphone=workphone)
    for name in ["", random_string("name", 10)]
    for lastname in ["", random_string("lastname", 10)]
    for address in ["", random_string("address", 10)]
    for email in ["", random_string("email", 10)]
    for mobilephone in ["", random_string("mobilephone", 10)]
    for workphone in ["", random_string("workphone", 10)]
]