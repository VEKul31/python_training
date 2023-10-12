from model.group import Group


def test_modification_first_group(app):
    app.session.login("admin", "secret")
    app.group.modification_first_group(Group("test2", "test2", "test2"))
    app.session.logout()
