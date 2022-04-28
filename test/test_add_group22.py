# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group11(app):
    app.manager_group.login(username="admin", password="secret")
    app.manager_group.create(Group(name="gfuy", header="ihhn", footer="fgh"))
    app.manager_group.logout()

def test_add_empty_group11(app):
    app.manager_group.login(username="admin", password="secret")
    app.manager_group.create(Group(name="", header="", footer=""))
    app.manager_group.logout()


