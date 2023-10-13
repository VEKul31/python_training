from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("name", "middlename",
                                   "lastname", "email"))
    app.contact.modify_first_contact(Contact("name2", "middlename2",
                                                   "lastname2", "email2"))

