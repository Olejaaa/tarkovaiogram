from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import state
import req

TOKEN = "1796570679:AAHzYZC6LFfpx5KvTUHrwpL11PRjI7gNgHc"

storage = MemoryStorage()
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start', "help"], state='*')
async def start(message: types.Message):
    await message.answer("Бля начало")


@dp.message_handler(commands=['ammo', 'пули'], state='*')
async def ammo_step1(message: types.Message):
    calibreBTN_list = [KeyboardButton('12x70mm'), KeyboardButton('20x70mm'), KeyboardButton('23x75mm'),
                       KeyboardButton('9x18mm Makarov'), KeyboardButton('7.62x25mm Tokarev'),
                       KeyboardButton('9x19mm Parabellum'), KeyboardButton('.45 ACP'), KeyboardButton('9x21mm Gyurza'),
                       KeyboardButton('5.7x28mm FN'), KeyboardButton('4.6x30mm HK'), KeyboardButton('9x39mm'),
                       KeyboardButton('.366 TKM'), KeyboardButton('5.45x39mm'), KeyboardButton('5.56x45mm NATO'),
                       KeyboardButton('.300 Blackout'), KeyboardButton('7.62x39mm'), KeyboardButton('7.62x51mm NATO'),
                       KeyboardButton('7.62x54mmR'), KeyboardButton('.338 Lapua Magnum'),
                       KeyboardButton('12.7x55mm STs-130'), KeyboardButton('40x46 mm')]

    ammo_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in calibreBTN_list:
        ammo_kb.add(i)

    await message.answer("Какой калибр?", reply_markup=ammo_kb)
    await state.ammo.get_bullet.set()


@dp.message_handler(commands=["барахолка", "market"], state='*')
async def market_step1(message: types.Message):
    await message.answer("Введите название предмета")
    await state.market.get_item.set()


@dp.message_handler(state=state.ammo.get_bullet)
async def ammo_step2(message: types.Message):
    try:
        output_ammo = req.get_ammo(message.text)
        for i in range(len(output_ammo)):
            await message.answer(
                f'Название: {output_ammo[i]["Name"]}\nУрон: {output_ammo[i]["Damage"]}\nВлияние на точность: {output_ammo[i]["Accuracy"]}\nВлияние на отдачу: {output_ammo[i]["Recoil"]}\nШанс фрагментации: {output_ammo[i]["Frag."]}\nПробитие брони 1-6 класа (максимально 6) :\n {output_ammo[i]["1"]} - {output_ammo[i]["2"]} - {output_ammo[i]["3"]} - {output_ammo[i]["4"]} - {output_ammo[i]["5"]} - {output_ammo[i]["6"]}')
    except Exception as e:
        await message.answer("Что-то пошло не так =(")


@dp.message_handler(state=state.market.get_item)
async def market_step2(message: types.Message):
    await message.answer("дай подумать...")
    try:
        output_items = req.get_market_items(message.text)
        for i in range(len(output_items)):
            # await bot.send_photo(message.chat.id, photo=)
            # await message.answer(f"Название: {output_items[i]['Name']}\nЦена: {output_items[i]['Price']}")
            await message.answer_photo(photo=output_items[i]['Src'],
                                       caption=f"Название: {output_items[i]['Name']}\nЦена: {output_items[i]['Price']}")
    except Exception as e:
        await message.answer("Что-то пошло не так =(")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
