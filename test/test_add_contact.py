from model.group import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Alex", lastname="Gubanov", nickname="Guban"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


# def test_add_empty_contact(app):
#    app.contact.create(Contact(firstname="", lastname="", nickname=""))
