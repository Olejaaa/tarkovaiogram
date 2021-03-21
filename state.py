from aiogram.dispatcher.filters.state import StatesGroup, State


class ammo(StatesGroup):
    get_bullet = State()


class market(StatesGroup):
    get_item = State()