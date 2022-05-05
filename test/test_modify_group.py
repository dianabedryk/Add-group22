from model.group import Group

def test_modify_group_name(app):
    app.manager_group.modify_first_group_name(Group(name="New group"))

def test_modify_group_header(app):
    app.manager_group.modify_first_group_header(Group(header="New header"))