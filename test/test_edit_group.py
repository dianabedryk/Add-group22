
from model.group import Edit_group

def test_edit_first_group(app):
    app.manager_group.edit_first_group(Edit_group(name="a", header="aa", footer="aaa"))