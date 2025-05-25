from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format, List
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

router = Router()


class StartSG(StatesGroup):
    start = State()

class ASG(StatesGroup):
    a = State()


# Хэндлер, обрабатывающий нажатие на кнопку 'Да'
async def yes_click_process(callback: CallbackQuery,
                            widget: Button,
                            dialog_manager: DialogManager):
    await callback.message.edit_text(
        text='<b>Прекрасно!</b>\n\nНадеюсь, вы найдете в этом курсе что-то '
             'новое и полезное для себя!'
    )
    await dialog_manager.done()


# Хэндлер, обрабатывающий нажатие на кнопку 'Нет'
async def no_click_process(callback: CallbackQuery,
                           widget: Button,
                           dialog_manager: DialogManager):
    await callback.message.edit_text(
        text='<b>Попробуйте!</b>\n\nСкорее всего, вам понравится!'
    )
    await dialog_manager.done()

async def get_items(**kwargs):
    return {'items': (
        (1, 'Пункт 1'),
        (2, 'Пункт 2'),
        (3, 'Пункт 3'),
    )}


# Это геттер
async def get_username(event_from_user: User, **kwargs):
    return {'username': event_from_user.username}


start_dialog = Dialog(
    Window(
        Format(text='Привет, <b>{username}</b>!\n'),
        Const(
            text='Пробовали ли вы уже писать ботов с использованием '
                 'библиотеки <code>aiogram_dialog</code>?'
        ),
        Row(
            Button(text=Const('✅ Да'), id='yes', on_click=yes_click_process),
            Button(text=Const('✖️ Нет'), id='no', on_click=no_click_process),
        ),
        getter=get_username,
        state=StartSG.start,
    ),
)

a_dialog = Dialog(
    Window(
        List(field=Format('{item[0]}. {item[1]}'),
             items='items'),
        getter=get_items,
        state=ASG.a,
    ),
)


# Это классический хэндлер, который будет срабатывать на команду /start
@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)

@router.message(Command(commands='a'))
async def command_a_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=ASG.a, mode=StartMode.RESET_STACK)


dp.include_router(router)
dp.include_router(start_dialog)
dp.include_router(a_dialog)
setup_dialogs(dp)
dp.run_polling(bot)