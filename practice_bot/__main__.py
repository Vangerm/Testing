import asyncio
import logging.config
from aiogram import Bot, Dispatcher

from .loger.logging_settings import logging_config
from .config_data.config import load_config
from .handlers import get_routers


logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)


async def main() -> None:
    logger.info('Starting bot')

    # Получаем конфигурационные данные
    config = load_config()

    # Активация телеграмм бота
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    dp.include_routers(*get_routers())

    # Запускаем polling
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logger.info('Stop bot')
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    asyncio.run(main())
