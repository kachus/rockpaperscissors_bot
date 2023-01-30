from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import LEXICON_RU

# creating a keyboard with yes and no answers to play a game
yes_no_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    resize_keyboard=True
)

button_yes: KeyboardButton = KeyboardButton(LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(LEXICON_RU['no_button'])



