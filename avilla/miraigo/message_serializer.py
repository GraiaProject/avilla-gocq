import base64
from copy import deepcopy

from avilla.miraigo.elements import TTS, CardImage, Gift, Poke, ShowImage
from avilla.onebot.message_serializer import onebot_msg_serializer

miraigo_msg_serializer = deepcopy(onebot_msg_serializer)


@miraigo_msg_serializer.register(ShowImage)
async def _showimage_serializer(element: ShowImage):
    return {
        "type": "image",
        "data": {
            "type": "show",
            "file": f"base64://{base64.b64encode(await element.provider()).decode('utf-8')}",
            "id": element.id,
        },
    }


@miraigo_msg_serializer.register(Poke)
async def _poke_serializer(element: Poke):
    return {"type": "poke", "data": {"qq": element.qq}}


@miraigo_msg_serializer.register(Gift)
async def _gift_serializer(element: Gift):
    return {
        "type": "gift",
        "data": {
            "qq": element.qq,
            "id": element.id,
        },
    }


@miraigo_msg_serializer.register(CardImage)
async def _cardimage_serializer(element: CardImage):
    return {
        "type": "cardimage",
        "data": {
            "file": f"base64://{base64.b64encode(await element.provider()).decode('utf-8')}",
            "minwidth": element.minwidth,
            "minheight": element.minheight,
            "maxwidth": element.maxwidth,
            "maxheight": element.maxheight,
            "source": element.source,
            "icon": element.icon,
        },
    }


@miraigo_msg_serializer.register(TTS)
async def _tts_serializer(element: TTS):
    return {"type": "tts", "data": {"text": element.text}}
