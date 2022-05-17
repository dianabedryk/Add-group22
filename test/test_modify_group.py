from model.group import Group

def test_modify_group_name(app):
    if app.manager_group.count() == 0:
        app.manager_group.create(Group(name="test"))
    old_groups = app.manager_group.get_group_list()
    app.manager_group.modify_first_group_name(Group(name="New group"))
    new_groups = app.manager_group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    if app.manager_group.count() == 0:
        app.manager_group.create(Group(name="test"))
    old_groups = app.manager_group.get_group_list()
    app.manager_group.modify_first_group_header(Group(header="New header"))
    new_groups = app.manager_group.get_group_list()
    assert len(old_groups) == len(new_groups)