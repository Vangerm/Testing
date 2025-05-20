import asyncio
import logging.config
from aiogram import Bot, Dispatcher

from .loger.logging_settings import logging_config
from .config_data.config import load_config
from .handlers import get_routers

from .lexicon.lexicon_ru import LEXICON_RU
from .lexicon.lexicon_en import LEXICON_EN

from .middlewares.i18n import TranslatorMiddleware


logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

translations = {
    'default': 'ru',
    'en': LEXICON_EN,
    'ru': LEXICON_RU,
}

async def main() -> None:
    logger.info('Starting bot')

    # Получаем конфигурационные данные
    config = load_config()

    # Активация телеграмм бота
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    dp.include_routers(*get_routers())

    # Подключаем внутренние миддлвары
    dp.update.middleware(TranslatorMiddleware())

    # Запускаем polling
    try:
        await dp.start_polling(
            bot,
            admin_ids=config.tg_bot.admin_ids,
            _translations=translations)
    except KeyboardInterrupt:
        logger.info('Stop bot')
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    asyncio.run(main())
