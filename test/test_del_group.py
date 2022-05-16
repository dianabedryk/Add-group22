from model.group import Group

def test_delete_first_group(app):
    if app.manager_group.count() == 0:
        app.manager_group.create(Group(name="test"))
    app.manager_group.delete_first_group()
