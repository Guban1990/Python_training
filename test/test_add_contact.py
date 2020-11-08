from model.group import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Alex", lastname="Gubanov", nickname="Guban"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", nickname=""))
