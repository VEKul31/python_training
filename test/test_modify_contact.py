from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("name", "middlename",
                                   "lastname", "email"))
    old_contacts = app.contact.get_contact_list()
    contacts = Contact(name="name2", lastname="lastname2")
    contacts.id = old_contacts[0].id
    app.contact.modify_first_contact(contacts)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

