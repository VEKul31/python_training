from model.contact import Contact
from model.group import Group
import random


def test_delete_some_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact("name", "middlename", "lastname",
                                   address="почтовый адрес", email="123", email2="234", email3="345",
                                   homephone="111", mobilephone="222", workphone="333", secondaryphone="444"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    if contact in orm.get_contact_not_in_group(group):
        app.contact.add_contact_to_group_by_id(contact.id, group.id)
    app.contact.delete_contact_from_group_by_id(contact.id, group.id)
    assert contact in orm.get_contact_not_in_group(group)
