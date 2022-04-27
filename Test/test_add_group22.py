# -*- coding: utf-8 -*-
import pytest
from Model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group11(app):
    app.session_group.login(username="admin", password="secret")
    app.group_creation(Group(name="gfuy", header="ihhn", footer="fgh"))
    app.session_group.logout()

def test_add_empty_group11(app):
    app.session_group.login(username="admin", password="secret")
    app.group_creation(Group(name="", header="", footer=""))
    app.session_group.logout()


