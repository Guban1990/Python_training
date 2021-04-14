from model.group import Contact
from random import randrange


def test_del_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Alexandr", lastname="Gubanov", nickname="Guban", address="Street",
                      homephone="+790999999", mobilephone="+7909123456", workphone="+89891234567",
                      secondaryphone="+79876654432", email="email@ya.ru", email2="mail2@r.ru", email3="mail3@rt.ru"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
