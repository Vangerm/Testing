import logging

from aiogram import Router, F
from aiogram.types import (
                            Message,
                            CallbackQuery,
                            InlineKeyboardButton,
                            InlineKeyboardMarkup)
from aiogram.filters import Command, CommandStart

from ..keyboards.keyboards import create_inline_kb
from ..lexicon.lexicon import BUTTONS


logger = logging.getLogger(__name__)

user_router = Router()

# Создаем объекты инлайн-кнопок
big_button_1 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed'
)

big_button_2 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]]
)

@user_router.message(CommandStart())
async def process_start_command(message: Message):
    logger.info(f'Пользователь {message.chat.username} ({message.chat.id}) запустил бота')
    await message.answer(text='У меня пока нет функционала')

@user_router.message(Command(commands='b'))
async def process_buttons_command(message: Message):
    await message.answer(
        text='У меня пока нет функционала',
        reply_markup=keyboard)

# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@user_router.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Ура! Нажата кнопка 1', show_alert=True)

# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_2_pressed'
@user_router.callback_query(F.data == 'big_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Ура! Нажата кнопка 2', show_alert=True)

@user_router.message(Command(commands='c'))
async def process_buttons_command(message: Message):
    keyboard = create_inline_kb(
    3,
    last_btn='back',
    **BUTTONS
)
    await message.answer(
        text='Это инлайн-клавиатура, сформированная функцией '
             '<code>create_inline_kb</code>',
        reply_markup=keyboard
    )

@user_router.message(Command(commands='getid'))
async def process_get_id_command(message: Message):
    await message.answer(text=str(message.chat.id))
