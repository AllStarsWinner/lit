from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Позивачам', callback_data='pozivacham')],
    [InlineKeyboardButton(text='Інвесторам', callback_data='investoram')],
    [InlineKeyboardButton(text='Адвокатам', callback_data='advokatam')],
    [InlineKeyboardButton(text='Наша команда', callback_data='nasha_komanda')],
    [InlineKeyboardButton(text='Бажаєте стати нашим представником?', callback_data='predstavnyk')],
    [InlineKeyboardButton(text='Відправити запит', callback_data='zapyt')],
    [InlineKeyboardButton(text='Контакти', callback_data='kontakty')]
])
pozer_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Позивачам/Відповідачам', callback_data='poz_pozer')],
    [InlineKeyboardButton(text='Позови, що фінансуються', callback_data='finans_pozer')],
    #[InlineKeyboardButton(text='Відправити запит', callback_data='zapyt_pozer')],
    [InlineKeyboardButton(text='Назад', callback_data='back')],
])

# === Кнопки для money ===
money_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Позивачам/Відповідачам', callback_data='poz_money')],
    [InlineKeyboardButton(text='Позови, що фінансуються', callback_data='finans_money')],
    [InlineKeyboardButton(text='Міжнародний досвід інвестицій в літігацію', callback_data='dosvid_money')],
    [InlineKeyboardButton(text='Принципи інвестицій в позови', callback_data='principy_money')],
    [InlineKeyboardButton(text='Назад', callback_data='back')],
])

# === Кнопки для lawyer ===
lawyer_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Адвокатам/Інфо', callback_data='advokat_lawyer')],
    [InlineKeyboardButton(text='Позови, що фінансуються', callback_data='finans_lawyer')],
    [InlineKeyboardButton(text='Назад', callback_data='back')],
])



back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад", callback_data="back")],
])