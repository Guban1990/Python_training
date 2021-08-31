from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    old_groups = db.get_group_list()
    edit_group = random.choice(old_groups)
    group = Group(name=f"Test name{random.randint(1000, 10000000)}", header="group_header_2", footer="group_footer_2")
    group.id = edit_group.id
    app.group.modify_group_by_id(edit_group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(edit_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



