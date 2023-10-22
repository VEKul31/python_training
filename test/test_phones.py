import re
from model.contact import Contact
from random import randrange


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("name", "middlename",
                                   "lastname", "email"))

    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def test_all_fields_on_home_page(app):
    random_contact = randrange(len(app.contact.get_contact_list()))
    all_info_contact_from_home_page = app.contact.get_contact_list()[random_contact]
    all_info_contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_contact)
    assert all_info_contact_from_home_page.firstname == all_info_contact_from_edit_page.firstname
    assert all_info_contact_from_home_page.lastname == all_info_contact_from_edit_page.lastname
    assert all_info_contact_from_home_page.all_addresses_from_home_page == all_info_contact_from_edit_page.address
    assert all_info_contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(all_info_contact_from_edit_page)
    assert all_info_contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(all_info_contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.workphone,
                                        contact.mobilephone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2,
                                        contact.email3]))))
