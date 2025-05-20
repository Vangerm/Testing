import logging

from aiogram.filters import BaseFilter
from aiogram.types import Message, TelegramObject

logger = logging.getLogger(__name__)


class IsAdmin(BaseFilter):

    async def __call__(self, message: Message, admin_ids: list) -> bool:
        return message.chat.id in admin_ids

class MyTrueFilter(BaseFilter):

    async def __call__(self, event: TelegramObject) -> bool:
        logger.debug('Попали внутрь фильтра %s', __class__.__name__)
        return True


class MyFalseFilter(BaseFilter):

    async def __call__(self, event: TelegramObject) -> bool:
        logger.debug('Попали внутрь фильтра %s', __class__.__name__)
        return False
