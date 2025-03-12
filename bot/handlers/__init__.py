from aiogram import Router
from . import user_handler


def get_routers() -> list[Router]:
    return [
        user_handler.router
    ]
