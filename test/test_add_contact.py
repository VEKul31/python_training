from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = (Contact("name", "middlename",  "lastname",
                                   address="почтовый адрес", email="123", email2="234", email3="345",
                                   homephone="111", mobilephone="222", workphone="333", secondaryphone="444"))
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
