# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group11(self):
    self.app.login(username="admin", password="secret")
    self.app.group_creation(Group(name="gfuy", header="ihhn", footer="fgh"))
    self.app.logout()

def test_add_empty_group11(self):
    self.app.login(username="admin", password="secret")
    self.app.group_creation(Group(name="", header="", footer=""))
    self.app.logout()


if __name__ == "__main__":
    unittest.main()
