from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup
from telebot.types import ReplyKeyboardMarkup


def get_main_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(True, False)
    keyboard.row('Баланс')
#    keyboard.row('Администратор')
    return keyboard


def get_cancel_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(True, False)
    keyboard.row('Отмена')
    return keyboard


def get_order_type_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(True, False)
    keyboard.row('Кэш', 'Транзит')
    keyboard.row('Отмена')
    return keyboard


def get_operation_type_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(True, False)
    keyboard.row('Строительство', 'Реклама', 'Прочее')
    keyboard.row('Выбрать фирму по ИНН')
    keyboard.row('Отмена')
    return keyboard


def get_inn_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(True, False)
    keyboard.row('Любую фирму')
    keyboard.row('Отмена')
    return keyboard


def get_document_inline_menu(user_id: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    data = {'Answer': True,
            'ID': user_id,
            'command': '',
            }
    callback_button1 = InlineKeyboardButton(text="Принять оплату",
                                            callback_data=str(data))
    data = {'Answer': False,
            'ID': user_id,
            'command': 'texting',
            }
    data = str(data)
    callback_button2 = InlineKeyboardButton(text="Отказать",
                                            callback_data=str(data))
    keyboard.add(callback_button1, callback_button2)
    return keyboard
