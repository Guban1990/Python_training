from model.group import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="New_firstname", lastname="New_lastname", nickname="New_nickname"))
    app.session.logout()
