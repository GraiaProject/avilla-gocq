from graia.broadcast.entities.dispatcher import BaseDispatcher
from graia.broadcast.interfaces.dispatcher import DispatcherInterface

from avilla.core.builtins.profile import FriendProfile
from avilla.core.entity import Entity
from avilla.core.event import AvillaEvent
from avilla.core.typing import T_Profile
from avilla.onebot.event import NudgeEvent


class FriendNudgeEvent(AvillaEvent[T_Profile]):
    operator: Entity[FriendProfile]

    class Dispatcher(BaseDispatcher):
        @staticmethod
        async def catch(interface: "DispatcherInterface"):
            return


class GroupNudgeEvent(NudgeEvent):
    pass


class MemberCardChanged(AvillaEvent[T_Profile]):
    # TODO
    pass
