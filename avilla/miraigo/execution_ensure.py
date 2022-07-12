import base64
from copy import deepcopy
from typing import TYPE_CHECKING

from avilla.onebot.execution_ensure import (_check_execution,
                                            _extract_and_check_as_groupid,
                                            _extract_and_check_as_memberid,
                                            ensure_execution)

from avilla.miraigo.execution import GroupPortraitSet

if TYPE_CHECKING:
    from avilla.miraigo.protocol import MiraigoProtocol

ensure_execution = deepcopy(ensure_execution)


@ensure_execution.override(execution=GroupPortraitSet, network="http")
async def set_group_portrait_http(self: "MiraigoProtocol", execution: GroupPortraitSet) -> None:
    group_id = _extract_and_check_as_groupid(execution.group)

    _check_execution(
        await self._http_post(
            "/set_group_portrait",
            {
                "group_id": group_id,
                "file": f"base64://{base64.b64encode(await execution.provider()).decode('utf-8')}",
            },
        )
    )


@ensure_execution.override(execution=GroupPortraitSet, network="ws")
async def set_group_portrait_ws(self: "MiraigoProtocol", execution: GroupPortraitSet) -> None:
    group_id = _extract_and_check_as_groupid(execution.group)

    _check_execution(
        await self._ws_client_send_packet(
            "set_group_portrait",
            {
                "group_id": group_id,
                "file": f"base64://{base64.b64encode(await execution.provider()).decode('utf-8')}",
            },
        )
    )
