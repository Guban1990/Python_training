import pytest
from model.group import Contact
from fixture.application import ApplicationContact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Alex", lastname="Gubanov", nickname="Guban"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", lastname="", nickname=""))
    app.session.logout()

