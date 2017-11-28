import telebot

import settings
import module_text as text
import module_db as db
import module_keyboard as keyboard


booker_bot = telebot.TeleBot(settings.TOKEN_BOOKER)


# Старт
@booker_bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    if db.access_check(user_id):
        response = 'Привет'
        booker_bot.send_message(user_id, response,
                                reply_markup=keyboard.get_main_menu())


# Обычное сообщение
@booker_bot.message_handler(func=lambda mesage: True, content_types=['text'])
def handle_text(message):
    user_id = message.from_user.id
    if db.access_check(user_id):
        state = db.get_state(user_id)
        response = text.handle_text(message, state)
        if response['markup']:
            # обычный ответ юзеру, но с обновлением клавиатуры
            booker_bot.send_message(user_id,
                                    response['text'],
                                    reply_markup=response['markup'],
                                    parse_mode='Markdown')
        else:
            # самый простой ответ юзеру
            booker_bot.send_message(user_id, response['text'],
                                    parse_mode='Markdown')


# сообщение c файлом
@booker_bot.message_handler(func=lambda mesage: True,
                            content_types=['document'])
def handle_doc(message):
    pass


# сообщение c фото
@booker_bot.message_handler(func=lambda mesage: True,
                            content_types=['photo'])
def handle_doc(message):
    pass


if __name__ == '__main__':
    booker_bot.polling(none_stop=True)
