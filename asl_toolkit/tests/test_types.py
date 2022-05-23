from asl_toolkit.types import SucceedState


def test_SucceedState():
    succeed_state = SucceedState()

    assert succeed_state.comment is None
    assert succeed_state.state_type == "Succeed"
    assert succeed_state.json == '{"Type": "Succeed"}'

    succeed_state = SucceedState(comment="A comment")

    assert succeed_state.comment == "A comment"
    assert succeed_state.state_type == "Succeed"
    assert succeed_state.json == '{"Type": "Succeed", "Comment": "A comment"}'
