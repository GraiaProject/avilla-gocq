from typing import Any, Dict, Final, List

from avilla.core.context import ctx_protocol
from avilla.core.execution import Execution
from avilla.core.message.chain import MessageChain
from avilla.core.platform import Platform
from avilla.miraigo.element_tree import ELEMENT_TYPE_MAP
from avilla.miraigo.message_serializer import miraigo_msg_serializer
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
        result = []

        with ctx_protocol.use(self):
            for x in data:
                elem_type = x["type"]
                elem_parser = ELEMENT_TYPE_MAP.get(elem_type)
                if elem_parser:
                    result.append(await elem_parser(x["data"]))
                else:
                    self.avilla.logger.error(f"message_parser: unexpected element type {elem_type}")

        return MessageChain.create(result)

    async def serialize_message(self, message: "MessageChain") -> List:
        return await miraigo_msg_serializer.serialize(message)

    async def ensure_execution(self, execution: Execution) -> Any:
        ...
