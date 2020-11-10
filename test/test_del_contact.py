from model.group import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test1", lastname="test2", nickname="test3"))
    app.contact.delete_first_contact()
