from model.contact import Contact
from model.group import Group
import random


def test_add_some_contact_in_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact("name", "middlename", "lastname",
                                   address="почтовый адрес", email="123", email2="234", email3="345",
                                   homephone="111", mobilephone="222", workphone="333", secondaryphone="444"))
    contacts = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)
