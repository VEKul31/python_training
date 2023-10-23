from model.contact import Contact
import pytest
import random
import string


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


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
