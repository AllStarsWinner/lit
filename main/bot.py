import asyncio
from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
import but
import os

from main import info
from aiogram import F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import re
from aiogram.types import FSInputFile
##########################################EXAMPLE HANDLER!!!!!!!!!!!!!!########################################################
"""
@dp.callback_query(F.data == '')
async def callback(callback: CallbackQuery):
    await callback.message.edit_text(, reply_markup=but.back)
"""
bot = Bot(token='7120184870:AAGj4MJH3Agf16KXvQvUoFG4JWcwNnfiOtE')  # Ініціалізуємо об'єкт бота з токеном
dp = Dispatcher()  # Ініціалізуємо диспетчер для обробки подій (команд, повідомлень тощо)

ADMIN_CHAT_ID = 892519055

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("""Офіційний чат-бот для порталу https://litigationfinanceportal.com

Фінансування позовів
Ми профінансуємо Ваш позов своїми коштами за певний відсоток судового виграшу. У випадку програшу нами процесу, ми не вимагатимемо від Вас повернення вкладених нами грошей""", parse_mode=ParseMode.HTML, reply_markup=but.main_inline)


@dp.callback_query(F.data == 'investoram')
async def callback_text1(callback: CallbackQuery):
    await callback.message.edit_text("Будь ласка, виберіть опцію яка Вас цікавить", reply_markup=but.money_inline, parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == 'advokatam')
async def callback(callback: CallbackQuery):
    await callback.message.edit_text("Будь ласка, виберіть опцію яка Вас цікавить", reply_markup=but.lawyer_inline, parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == 'pozivacham')
async def callback(callback: CallbackQuery):
    await callback.message.edit_text("Будь ласка, виберіть опцію яка Вас цікавить", reply_markup=but.pozer_inline)


@dp.callback_query(F.data == 'advokat_lawyer')
async def callback(callback: CallbackQuery):
    await callback.message.edit_text(info.lawyer, reply_markup=but.back)



@dp.callback_query(F.data == 'predstavnyk')
async def callback(callback: CallbackQuery):
    await callback.message.edit_text(info.pred, reply_markup=but.back, parse_mode=ParseMode.HTML)

@dp.callback_query(F.data == 'nasha_komanda')
async def callback(callback: CallbackQuery):
    await callback.message.edit_text(info.site,reply_markup=but.back)



@dp.callback_query(F.data == 'spez')
async def asd(callback: CallbackQuery):
    await callback.message.edit_text("Будь ласка, виберіть опцію яка Вас цікавить", reply_markup=but.spez)


@dp.callback_query(F.data == 'bank')
async def call(callback: CallbackQuery):
    await callback.message.edit_text(info.bank, reply_markup=but.back)


@dp.callback_query(F.data == 'patent')
async def ytsd(callback: CallbackQuery):
    await callback.message.edit_text(info.patent, reply_markup=but.back)



@dp.callback_query(F.data == 'moskal')
async def asddasdl(callback: CallbackQuery):
    await callback.message.edit_text(info.moskal, reply_markup=but.back)

@dp.callback_query(F.data == 'zapyt')
async def cmd_anketa(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""📑 Анкета

Надайте відповідь на наступні запитання 👇""")
    await callback.message.answer("Прізвище ім'я по-батькові")
    await state.set_state(RecruitingForm.PIB)


class RecruitingForm(StatesGroup):
    PIB = State()
    phone = State()
    komentar = State()  # итоговый комментарий


@dp.callback_query(F.data == 'anketa')
async def cmd_anketa(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("📑 Анкета\n\nНадайте відповідь на наступні запитання 👇")
    await callback.message.answer("Прізвище ім'я по-батькові")
    await state.set_state(RecruitingForm.PIB)


@dp.message(RecruitingForm.PIB)
async def cmd_pib(message: Message, state: FSMContext):
    await state.update_data(PIB=message.text)
    await message.answer("📱 Номер телефону\n\nℹ️ Введіть його у міжнародному форматі +380XXXXXXXXX 👇")
    await state.set_state(RecruitingForm.phone)


def is_valid_phone(phone: str) -> bool:
    return bool(re.match(r'^\+?\d{10,15}$', phone))


@dp.message(RecruitingForm.phone)
async def cmd_phone(message: Message, state: FSMContext):
    if not is_valid_phone(message.text):
        await message.answer("❌ Увведений некоректний номер телефону. Спробуйте ще раз.")
        return
    await state.update_data(phone=message.text)
    await message.answer("💬 Будь ласка, напишіть який у Вас позов")
    await state.set_state(RecruitingForm.komentar)


@dp.message(RecruitingForm.komentar)
async def cmd_komentar(message: Message, state: FSMContext):
    await state.update_data(komentar=message.text)

    data = await state.get_data()
    user_data_message = (
        f"📥 Нова анкета:\n\n"
        f"👤 Прізвище, ім'я, по-батькові: {data['PIB']}\n"
        f"📞 Номер телефону: {data['phone']}\n"
        f"💬 Коментар: {data['komentar']}"
    )

    await message.answer("✅ Дякуємо! Вашу анкету надіслано. Очікуйте на відповідь.", reply_markup=but.main_inline)
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text=user_data_message)
    await state.clear()



@dp.callback_query(F.data =='back')
async def cmd_start(callback: CallbackQuery):
    await callback.message.edit_text("""Офіційний чат-бот для порталу https://litigationfinanceportal.com

Фінансування позовів
Ми профінансуємо Ваш позов своїми коштами за певний відсоток судового виграшу. У випадку програшу нами процесу, ми не вимагатимемо від Вас повернення вкладених нами грошей""", reply_markup=but.main_inline, parse_mode=ParseMode.HTML)
################################################## MAIN BUTTONS END!!!!!!!!!###########################################################################
################################################## POZER INLINE START!!!!!!!###########################################################################

@dp.callback_query(F.data == 'poz_pozer')
async def handle_poz_pozer(callback: CallbackQuery):
    await callback.message.edit_text(info.pozer, reply_markup=but.back)

@dp.callback_query(F.data == 'finans_pozer')
async def handle_finans_pozer(callback: CallbackQuery):
    await callback.message.edit_text(info.pozer, reply_markup=but.back, parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == 'poz_money')
async def handle_poz_money(callback: CallbackQuery):
    await callback.message.edit_text(info.money, reply_markup=but.back)

@dp.callback_query(F.data == 'finans_money')
async def asdawd(callback: CallbackQuery):
    await callback.message.edit_text(info.sofi, reply_markup=but.back)

@dp.callback_query(F.data == 'dosvid_money')
async def handle_dosvid_money(callback: CallbackQuery):
    await callback.message.edit_text(info.sudV2, reply_markup=but.back)

@dp.callback_query(F.data == 'principy_money')
async def handle_principy_money(callback: CallbackQuery):
    await callback.message.edit_text(info.sofi, reply_markup=but.back)

@dp.callback_query(F.data == 'call_money')
async def handle_call_money(callback: CallbackQuery):
    await callback.message.edit_text("📞 Зателефонуйте нам: +38 0672098020 або напишіть нам на емейл vbfunds@gmail.com", reply_markup=but.back)

@dp.callback_query(F.data == 'kontakty')
async def callback(callback: CallbackQuery):
    await callback.message.edit_text(info.contact, reply_markup=but.back)




@dp.callback_query(F.data == 'back')
async def asdg(callback: CallbackQuery):
    await callback.message.edit_text(info.welcome, reply_markup=but.main_inline)














async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())