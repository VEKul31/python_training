from model.contact import Contact
import re


def test_all_contacts_on_homepage(app, db):
    contact_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_ui)):
        assert contact_ui[i].id == contact_db[i].id
        assert contact_ui[i].name == contact_db[i].name
        assert contact_ui[i].lastname == contact_db[i].lastname
        assert contact_ui[i].address == contact_db[i].address
        assert contact_ui[i].all_emails_from_home_page == merge_emails_like_on_homepage(contact_db[i])
        assert contact_ui[i].all_phones_from_home_page == merge_phones_like_on_homepage(contact_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))
