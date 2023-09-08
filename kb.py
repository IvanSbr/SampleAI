from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


# Main menu set up

main_menu = [
    [InlineKeyboardButton(text="🎶 Загрузить аудиодорожку", callback_data="upload_audio")],

    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help"),
    InlineKeyboardButton(text="💰 Поддержать", callback_data="support")]

]
main_menu = InlineKeyboardMarkup(inline_keyboard=main_menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="main_menu")]])


# Audio menu set up
audio_menu = [
    [InlineKeyboardButton(text="1", callback_data="1"), InlineKeyboardButton(text="2", callback_data="2")],
    [InlineKeyboardButton(text="3", callback_data="3"), InlineKeyboardButton(text="4", callback_data="4")]
]
audio_menu = InlineKeyboardMarkup(inline_keyboard=audio_menu)
exit_audio_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в  аудио меню")]], resize_keyboard=True)
iexit_audio_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в аудио меню", callback_data="audio_menu")]])