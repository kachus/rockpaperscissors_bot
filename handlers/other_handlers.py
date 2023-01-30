from aiogram import Dispatcher
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU

async def send_answer(messsage: Message):
    await messsage.answer(text=LEXICON_RU['other_answer'])

async def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(send_answer)

#handlers which handle everything beyond the basic functional
