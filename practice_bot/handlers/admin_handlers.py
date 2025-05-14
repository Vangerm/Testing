import logging

from aiogram import Router
from aiogram.types import (
                            Message,
                            FSInputFile)
from aiogram.filters import Command

from ..filters.filters import IsAdmin


logger = logging.getLogger(__name__)

admin_router = Router()


# Получение логер файла
@admin_router.message(Command(commands='getlog'), IsAdmin())
async def admin_get_log_command(message: Message):
    await message.answer_document(FSInputFile('bot/loger/logs.log'))
