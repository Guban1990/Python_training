from model.group import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="New_firstname1", lastname="New_lastname2", nickname="New_nickname3"))
    app.contact.edit_first_contact(Contact(firstname="New_firstname", lastname="New_lastname", nickname="New_nickname"))
