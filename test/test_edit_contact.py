from model.group import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Alex2", lastname="Gubanov2", nickname="Guban2"))
    app.session.logout()
