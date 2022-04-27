# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group11(app):
    app.app.login(username="admin", password="secret")
    app.app.group_creation(Group(name="gfuy", header="ihhn", footer="fgh"))
    app.app.logout()

def test_add_empty_group11(app):
    app.app.login(username="admin", password="secret")
    app.app.group_creation(Group(name="", header="", footer=""))
    app.app.logout()


