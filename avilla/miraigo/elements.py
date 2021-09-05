from typing import Optional

from avilla.core.builtins.elements import Image, Text
from avilla.core.message.element import Element
from avilla.core.provider import Provider

__all__ = (
    "ShowImage",
    "Poke",
    "RedBag",
    "Gift",
    "CardImage",
    "TTS",
)


class ShowImage(Image):
    id: int

    def __init__(self, provider: Provider, id: int = None):
        super().__init__(provider)
        self.id = id

    def asDisplay(self) -> str:
        return f"[$miraigo::ShowImage:id={self.id}]"


class Poke(Element):
    qq: int

    def __init__(self, qq: int):
        self.qq = qq

    def asDisplay(self) -> str:
        return f"[$miraigo::Poke:qq={self.qq}]"


class RedBag(Element):
    title: str

    def __init__(self, title: str):
        self.title = title

    def asDisplay(self) -> str:
        return f"[$miraigo::RedBag:title={self.title}]"


class Gift(Element):
    qq: int
    id: int

    def __init__(self, qq: int, id: int):
        self.qq = qq
        self.id = id

    def asDisplay(self) -> str:
        return f"[$miraigo::Gift:qq={self.qq},id={self.id}]"


class CardImage(Image):
    minwidth: Optional[int] = None
    minheight: Optional[int] = None
    maxwidth: Optional[int] = None
    maxheight: Optional[int] = None
    source: Optional[str] = None
    icon: Optional[str] = None

    def __init__(
        self,
        provider: Provider,
        minwidth: Optional[int] = None,
        minheight: Optional[int] = None,
        maxwidth: Optional[int] = None,
        maxheight: Optional[int] = None,
        source: Optional[str] = None,
        icon: Optional[str] = None,
    ):
        super().__init__(provider)
        self.minwidth = minwidth
        self.minheight = minheight
        self.maxwidth = maxwidth
        self.maxheight = maxheight
        self.source = source
        self.icon = icon

    def asDisplay(self) -> str:
        return (
            f"[$miraigo::CardImage:"
            f"minwidth={self.minwidth or 'null'},"
            f"minheight={self.minheight or 'null'}"
            f"maxwidth={self.maxwidth or 'null'},"
            f"maxheight={self.maxheight or 'null'}"
            f"source={self.source or 'null'}"
            f"icon={self.icon or 'null'}"
        )


class TTS(Text):
    def asDisplay(self) -> str:
        return f"[$miraigo::TTS:text={self.text}]"
