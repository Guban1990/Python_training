from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Test name2", header="Test header2", footer="test comment2"))
    app.session.logout()
