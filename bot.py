import asyncio  # Імпортуємо модуль для роботи з асинхронністю
from aiogram import Bot, Dispatcher, F  # Імпортуємо необхідні компоненти з бібліотеки aiogram
from aiogram.types import Message, FSInputFile  # Імпортуємо типи повідомлень та файлів
from aiogram.filters import CommandStart, Command  # Імпортуємо фільтри для обробки команд
import app  # Імпортуємо локальний модуль app (напевно, частина твого проєкту)
import info  # Імпортуємо модуль info (напевно, частина твого проєкту)
from aiogram.enums import ParseMode  # Імпортуємо перерахування для режиму форматування тексту (Markdown або HTML)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from dibil import init_db, add_user, get_user
from dibil import add_user
from selector import router


bot = Bot(token='7120184870:AAGj4MJH3Agf16KXvQvUoFG4JWcwNnfiOtE')  # Ініціалізуємо об'єкт бота з токеном
dp = Dispatcher()  # Ініціалізуємо диспетчер для обробки подій (команд, повідомлень тощо)

ADMIN_CHAT_ID = 6155988964


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(info.euro, parse_mode=ParseMode.HTML, reply_markup=app.main)

@dp.message(F.text == 'Позивачам')
async def cmd_text1(message: Message):
    await message.answer('Виберіть категорію яка Вам потрібна',parse_mode=ParseMode.MARKDOWN_V2, reply_markup=app.pozer)



@dp.message(F.text == 'Зробити дзвінок')
async def cmd_text1(message: Message):
    await message.answer(info.pozerContact)



@dp.message(F.text == 'Інвесторам')
async def cmd_text1(message: Message):
    await message.answer('Виберіть категорію яка Вам потрібна', reply_markup=app.money)


@dp.message(F.text == 'Адвокатам')
async def cmd_text1(message: Message):
    await message.answer('Виберіть категорію яка Вам потрібна', reply_markup=app.lawyer)


@dp.message(F.text == 'Наша команда')
async def cmd_text1(message: Message):
    await message.answer(info.CBO)


@router.message(F.text == 'Контакти')
async def cmd_text1(message: Message):
    await message.answer(info.contact,parse_mode=ParseMode.HTML)


@dp.message(F.text == 'Допомога менеджера')
async def cmd_text1(message: Message):
    await message.answer(info.dollar)


@dp.message(F.text == 'Про нас')
async def cmd_text1(message: Message):
    await message.answer('')


@dp.message(F.text == '')
async def cmd_text1(message: Message):
    await message.answer('')


@dp.message(F.text == 'Бажаєте стати нашим представником?')
async def cmd_text1(message: Message):
    await message.answer(info.kiev)


@dp.message(F.text == 'Назад')
async def cmd_text1(message: Message):
    await message.answer('Назад', reply_markup=app.main)

@dp.message(F.text == 'Позивачам/Відповідачам')
async def cmd_text1(message: Message):
    await message.answer(info.pozer,parse_mode=ParseMode.HTML)





@dp.message(F.text == 'Інвесторам/Інфо')
async def cmd_text1(message: Message):
    await message.answer(info.money,parse_mode=ParseMode.HTML)


@dp.message(F.text == 'Принципи інвестицій в позови')
async def cmd_text1(message: Message):
    await message.answer(info.sud,parse_mode=ParseMode.HTML)
    await message.answer(info.sudV2,parse_mode=ParseMode.HTML)
    await message.answer(info.sudV3,parse_mode=ParseMode.HTML)

@dp.message(F.text == 'Адвокатам/Інфо')
async def cmd_text1(message: Message):
    await message.answer(info.lawyer, parse_mode=ParseMode.HTML)




@dp.message(F.text == 'ЗМІ про нас')
async def cmd_text1(message: Message):
    await message.answer(info.CBO)


@dp.message(F.text == 'Світ інвестицій')
async def cmd_text1(message: Message):
    await message.answer(info.invest)







@dp.message(F.text == 'Міжнародний досвід інвестицій в літігацію')
async def cmd_text1(message: Message):
    await message.answer(info.invest)
################################################# FORMA
class Form(StatesGroup):
    name = State()
    surname = State()
    age = State()
    nomer = State()
    question = State()


@dp.message(F.text == 'Відправити запит')
async def cmd_text1(message: Message,state: FSMContext):
    await message.answer('Уведіть будь ласка Ваше ім\'я')
    await state.set_state(Form.name)
# карочи имя
@dp.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    name = message.text.strip()
    if not name.isalpha():
        await message.answer("Ім'я повинно містити лише букви. Спробуйте ще раз:")
        return
    await state.update_data(name=name)
    await message.answer("Введіть своє прізвище:")
    await state.set_state(Form.surname)
    # карочи фамилия
@dp.message(Form.surname)
async def process_surname(message: Message, state: FSMContext):
    surname = message.text.strip()
    if not surname.isalpha():
        await message.answer("Прізвище повинно містити лише букви. Спробуйте ще раз:")
        return
    await state.update_data(surname=surname)
    await message.answer("Введіть свій вік (тільки число):")
    await state.set_state(Form.age)

# карочи старый
@dp.message(Form.age)
async def process_age(message: Message, state: FSMContext):
    age = message.text.strip()
    if not age.isdigit() or not (1 <= int(age) <= 120):
        await message.answer("Вік має бути числом від 1 до 120. Спробуйте ще раз:")
        return
    await state.update_data(age=int(age))
    await message.answer("Уведіть контактний номер телефону")
    await state.set_state(Form.nomer)

@dp.message(Form.nomer)
async def process_age(message: Message, state: FSMContext):
    nomer = message.text.strip()
    if not nomer:
        await message.answer("Невірно введений номер. Спробуйте ще раз:")
        return
    await state.update_data(nomer=nomer)
    await message.answer("Напишіть Ваш запит")
    await state.set_state(Form.question)

@dp.message(Form.question)
async def process_age(message: Message, state: FSMContext):
    question = message.text.strip()
    if not question:
        await message.answer("Не зрозуміла інформація")
        return
    await state.update_data(question=question)
# Отримання даних
    global user_data
    user_data = await state.get_data()
    await add_user(message.from_user.id, user_data["name"], user_data["surname"], user_data["age"], user_data["nomer"], user_data["question"])

    user_data_message = (
        f"Дякую за інформацію!\n"
        f"Ім'я: {user_data['name']}\n"
        f"Прізвище: {user_data['surname']}\n"
        f"Вік: {user_data['age']}\n"
        f"Номер телефону:{user_data['nomer']}\n"
        "Ваш запит взятий в обробку\n"
        f"{user_data['question']}\n")
    # Відповідь користувачу
    await message.answer(user_data_message)

    # Надсилання адміністратору
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text=user_data_message)

    # Завершення стану
    await state.clear()
######################################################### db

@dp.message(F.text == '')
async def cmd_text1(message: Message):
    await message.answer('')


@dp.message(F.text == '')
async def cmd_text1(message: Message):
    await message.answer('')


async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот виключений')