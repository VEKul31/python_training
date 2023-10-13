from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("name", "middlename",
                                   "lastname", "email"))
    app.contact.delete_first_contact()
