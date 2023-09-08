from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    '''
    Message '/start' -> main menu 
    '''
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.main_menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def main_menu(msg: Message):
    await msg.answer(text.main_menu, reply_markup=kb.main_menu)



@router.callback_query(F.data == 'upload_audio')
async def audio_menu(callback: types.CallbackQuery):
    '''
    After pushing '🎶 Загрузить аудиодорожку' button raises audio menu
    '''
    await callback.message.answer(text.audio_menu, reply_markup=kb.audio_menu)
    await callback.answer()

@router.callback_query(F.data == "help")
async def help_button(callback: types.CallbackQuery):
    await callback.message.answer("Данный бот позволяет разложить песню на составляющие или выделить нужный тебе инструмент")
    await callback.answer()

@router.callback_query(F.data == 'support')
async def support_button(callback: types.CallbackQuery):
    await callback.message.answer(" Чтобы поддержать данный проект свяжись с одним из его создателей:\
                                   \n @sasha_doroshkevich \n @roman_dvoryankov \n @polozhiev \
                                   \n @noonmare \n @ivansbrodov") 
    await callback.answer()

@router.callback_query(F.data ==  "return_1")
async def audio_to_main(callback: types.CallbackQuery):
    await callback.message.answer(text.main_menu, reply_markup=kb.main_menu)
    await callback.answer()

@router.callback_query(F.data ==  "selection")
async def audio_to_select(callback: types.CallbackQuery):
    await callback.message.answer(text=text.select_menu)
    await callback.answer()


# @router.callback_query(F.data ==  "return_2")
# async def select_to_audio(callback: types.CallbackQuery):
#     await callback.message.answer(text.audio_menu, reply_markup=kb.audio_menu)
#     await callback.answer()


@router.callback_query(F.data == "decomposition")
async def audio_decomp(callback: types.CallbackQuery):
    await callback.message.answer("Можешь прислать в чат песню, которую хотел бы разложить")
    await callback.answer()
