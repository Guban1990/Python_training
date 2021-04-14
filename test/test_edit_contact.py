from model.group import Contact
from random import randrange

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Alexandr", lastname="Gubanov", nickname="Guban", address="Street",
                      homephone="+790999999", mobilephone="+7909123456", workphone="+89891234567",
                      secondaryphone="+79876654432", email="email@ya.ru", email2="mail2@r.ru", email3="mail3@rt.ru"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Alexandr_QA", lastname="Gubanov", nickname="Guban", address="Street",
                      homephone="+790999999", mobilephone="+7909123456", workphone="+89891234567",
                      secondaryphone="+79876654432", email="email@ya.ru", email2="mail2@r.ru", email3="mail3@rt.ru")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
