from aiogram import Router

from . import user
from . import admin
from . import other


def get_routers() -> list[Router]:
    return [
        user.user_router,
        admin.admin_router,
        other.other_router  # other_handlers - должен быть последним
    ]
