from model.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.manager_group.count() == 0:
        app.manager_group.create(Group(name="test"))
    old_groups = app.manager_group.get_group_list()
    index = randrange(len(old_groups))
    app.manager_group.delete_group_by_index(index)
    new_groups = app.manager_group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups
