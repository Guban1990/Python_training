from model.group import Contact
from random import randrange

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="New_firstname1", lastname="New_lastname2", nickname="New_nickname3"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New_firstname", lastname="New_lastname", nickname="New_nickname")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
