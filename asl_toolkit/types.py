import json
from abc import ABC
from typing import Optional, Dict


class _BaseState(ABC):
    def __init__(self, state_type: str, comment: Optional[str] = None):
        self.state_type = state_type
        self.comment = comment

    def construct_state(self) -> Dict[str, str]:
        state = {
            "Type": self.state_type,
        }

        if self.comment is not None:
            state["Comment"] = self.comment

        return state

    @property
    def json(self) -> str:
        return json.dumps(self.construct_state())


class SucceedState(_BaseState):
    def __init__(self, comment: Optional[str] = None):
        """
        Implementation of SucceedState.

        https://states-language.net/spec.html#succeed-state

        Args:
            comment: Human readable comment
        """
        super().__init__(state_type="Succeed", comment=comment)
