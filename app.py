from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Позивачам'), KeyboardButton(text='Інвесторам')],
        [KeyboardButton(text='Адвокатам'), KeyboardButton(text='Наша команда')],
        [KeyboardButton(text='Бажаєте стати нашим представником?')],
        [KeyboardButton(text='Відправити запит')],
        [KeyboardButton(text='Контакти')]
    ]
)

pozer = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Позивачам/Відповідачам')],
        [KeyboardButton(text='Позови, що фінансуються')],
        [KeyboardButton(text='Відправити запит')],
        [KeyboardButton(text='Назад')]
    ]
)



money = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Позивачам/Відповідачам')],
        [KeyboardButton(text='Позови, що фінансуються')],
        [KeyboardButton(text='Міжнародний досвід інвестицій в літігацію')],
        [KeyboardButton(text='Принципи інвестицій в позови')],  # Додана кнопка
        [KeyboardButton(text='Зробити дзвінок')],
        [KeyboardButton(text='Назад')]  # Додана кнопка
    ]
)


lawyer = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Адвокатам/Інфо')],
                                      [KeyboardButton(text='Позови, що фінансуються')],
                                      [KeyboardButton(text='Назад')]])






