from typing import Any, Dict, Final, List

from avilla.core.execution import Execution
from avilla.core.message.chain import MessageChain
from avilla.core.platform import Platform
from avilla.onebot.protocol import OnebotProtocol


class MiraigoProtocol(OnebotProtocol):
    platform: Final[Platform] = Platform(  # type: ignore
        name="Tencent QQ",
        protocol_provider_name="miraigo",
        implementation="OneBot",
        supported_impl_version="v11",
        generation="11",
    )

    async def has_ability(self, ability: str) -> bool:
        ...

    async def parse_message(self, data: List[Dict]) -> "MessageChain":
        ...

    async def serialize_message(self, message: "MessageChain") -> List:
        ...

    async def ensure_execution(self, execution: Execution) -> Any:
        ...
