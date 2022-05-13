
import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.manager_group.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.manager_group.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def fin():
        fixture.manager_group.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture