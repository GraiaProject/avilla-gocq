from typing import Union

from avilla.core.builtins.profile import GroupProfile
from avilla.core.contactable import Contactable, ref
from avilla.core.execution import Execution, Operation
from avilla.core.provider import Provider


class GroupPortraitSet(Operation, Execution):
    group: Union[Contactable[GroupProfile], ref, str]
    provider: Provider

    def __init__(self, group: Union[Contactable[GroupProfile], ref, str], provider: Provider):
        super().__init__(group, provider)
