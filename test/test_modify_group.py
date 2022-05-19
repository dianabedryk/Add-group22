from model.group import Group

def test_modify_group_name(app):
    if app.manager_group.count() == 0:
        app.manager_group.create(Group(name="test"))
    old_groups = app.manager_group.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.manager_group.modify_first_group_name(group)
    new_groups = app.manager_group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.manager_group.count() == 0:
#       app.manager_group.create(Group(name="test"))
#    old_groups = app.manager_group.get_group_list()
#    group = Group(header="New header")
#    group.id = old_groups[0].id
#   app.manager_group.modify_first_group_header(group)
#    new_groups = app.manager_group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


