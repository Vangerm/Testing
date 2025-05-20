import logging

from aiogram import Router
from aiogram.types import (
                            Message,
                            FSInputFile)
from aiogram.filters import Command

from ..filters.filters import IsAdmin


logger = logging.getLogger(__name__)

admin_router = Router()

admin_router.message.filter(IsAdmin())


# Получение логер файла
@admin_router.message(Command(commands='getlog'))
async def admin_get_log_command(message: Message):
    await message.answer_document(FSInputFile('practice_bot/loger/logs.log'))
