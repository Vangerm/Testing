import logging

from aiogram import Router, F, Bot
from aiogram.types import (
                            Message,
                            CallbackQuery,
                            InlineKeyboardButton,
                            InlineKeyboardMarkup)
from aiogram.filters import Command, CommandStart
from ..filters.filters import MyTrueFilter, MyFalseFilter


logger = logging.getLogger(__name__)

user_router = Router()

# Этот хэндлер срабатывает на команду /start
@user_router.message(CommandStart(), MyTrueFilter())
async def process_start_command(message: Message, i18n: dict[str, str]) -> None:
    logger.debug('Вошли в хэндлер, обрабатывающий команду /start')
    # Создаем объект инлайн-кнопки
    button = InlineKeyboardButton(
        text=i18n['button'],
        callback_data='button_pressed'
    )
    # Создаем объект инлайн-клавиатуры
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    # Отправляем сообщение пользователю
    await message.answer(text=i18n['/start'], reply_markup=markup)
    logger.debug('Выходим из хэндлера, обрабатывающего команду /start')


# Этот хэндлер срабатывает на нажатие инлайн-кнопки
@user_router.callback_query(F.data, MyTrueFilter())
async def process_button_click(callback: CallbackQuery, i18n: dict[str, str], bot: Bot) -> None:
    logger.debug('Вошли в хэндлер, обрабатывающий нажатие на инлайн-кнопку')
    # await callback.answer(text=i18n['button_pressed'])
    await bot.send_message(chat_id=469873066, text='111')
    logger.debug('Выходим из хэндлера, обрабатывающего нажатие на инлайн-кнопку')


# Это хэндлер, который мог бы обрабатывать любой текст,
# но `MyFalseFilter` его не пропустит
@user_router.message(F.text, MyFalseFilter())
async def process_text(message: Message, bot: Bot) -> None:
    logger.debug('Вошли в хэндлер, обрабатывающий текст')
    logger.debug('Выходим из хэндлера, обрабатывающего текст')
    await bot.send_message(chat_id=469873066, text='111')