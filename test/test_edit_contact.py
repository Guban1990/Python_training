from model.group import Contact
import random


def test_edit_contact(app, db, check_ui):
    if  len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Alexandr", lastname="Gubanov", nickname="Guban", address="Street",
                      homephone="+790999999", mobilephone="+7909123456", workphone="+89891234567",
                      secondaryphone="+79876654432", email="email@ya.ru", email2="mail2@r.ru", email3="mail3@rt.ru"))
    old_contacts = db.get_contact_list()
    edit_contact = random.choice(old_contacts)
    contact = Contact(firstname="Alexandr_QA", lastname="Gubanov", nickname="Guban", address="Street",
                      homephone="+790999999", mobilephone="+7909123456", workphone="+89891234567",
                      secondaryphone="+79876654432", email="email@ya.ru", email2="mail2@r.ru", email3="mail3@rt.ru")
    contact.id = edit_contact.id
    app.contact.edit_contact_by_id(edit_contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(edit_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
