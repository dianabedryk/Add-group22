

from model.group import Group




def test_add_group(app):
    old_groups = app.manager_group.get_group_list()
    group = Group(name="gfuy", header="ihhn", footer="fgh")
    app.manager_group.create(group)
    assert len(old_groups) + 1 == app.manager_group.count()
    new_groups = app.manager_group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_add_empty_group(app):
#    old_groups = app.manager_group.get_group_list()
#    group = Group(name="", header="", footer="")
#    app.manager_group.create(group)
#    new_groups = app.manager_group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

