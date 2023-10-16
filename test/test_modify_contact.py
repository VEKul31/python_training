from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("name", "middlename",
                                   "lastname", "email"))
    app.contact.modify_first_contact(Contact(name="name2", lastname="lastname2"))



