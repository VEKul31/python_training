from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("name", "middlename",  "lastname",
                                   address="почтовый адрес", email="123", email2="234", email3="345",
                                   homephone="111", mobilephone="222", workphone="333", secondaryphone="444"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
