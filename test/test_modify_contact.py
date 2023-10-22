from model.contact import Contact
from random import randrange


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("name", "middlename",  "lastname",
                                   address="почтовый адрес", email="123", email2="234", email3="345",
                                   homephone="111", mobilephone="222", workphone="333", secondaryphone="444"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contacts = Contact(name="name2", lastname="lastname2")
    contacts.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contacts)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

