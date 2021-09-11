from typing import Awaitable, Callable, Dict

from avilla.core.builtins.elements import Image
from avilla.core.message.element import Element
from avilla.core.provider import HttpGetProvider
from avilla.miraigo.elements import Poke, RedBag, ShowImage
from avilla.onebot.element_tree import ELEMENT_TYPE_MAP
from avilla.onebot.elements import FlashImage

ELEMENT_TYPE_MAP = ELEMENT_TYPE_MAP.copy()


def register(element_type: str):
    def wrapper(func: Callable[[Dict], Awaitable[Element]]):
        ELEMENT_TYPE_MAP[element_type] = func
        return func

    return wrapper


@register("image")
async def image(data: Dict):
    type = data.get("type")
    if type == "flash":
        return FlashImage(HttpGetProvider(data["url"]))
    elif type == "show":
        return ShowImage(HttpGetProvider(data["url"]))
    return Image(HttpGetProvider(data["url"]))


@register("redbag")
async def redbag(data: Dict):
    return RedBag(data["title"])


@register("poke")
async def poke(data: Dict):
    return Poke(data["qq"])
