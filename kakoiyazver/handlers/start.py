import logging
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()
logger = logging.getLogger("kakoiyazver_bot.start")

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = message.from_user
    logger.info(f"Пользователь {user.id} (@{user.username or user.full_name}) нажал /start")
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Начать викторину", callback_data="start_quiz")]
    ])
    await message.answer(
        "Узнай свое тотемное животное \nГотов пройти викторину?",
        reply_markup=kb
    )