import settings
import module_keyboard as keyboard
import module_db as db

# =========================================================================== #
# Все все ответы собираются здесь. В зависимости от состояния юзера           #
# вызывается соответсвующая функция. В ответ каждая функция отдаёт словарь    #
# следующего формата:                                                         #
# Text = текст сообщения от бота;                                             #
# Markup = нужно ли обновление клавиатуры, и какое;                           #
# Send = Сообщение мэнеджеру;                                                 #
# =========================================================================== #


def error_text() -> dict:
    response = 'Haha'
    markup = False
    ret = {'text': response,
           'markup': markup,
           }
    return ret

def start() -> dict:
    commands = {'Баланс': balance_menu}
    return commands.get(mess.text, error_text)()

def balance_menu() -> dict:

    balance = db.det_balance()

    response = f'Ваш баланс: {balance}'
    markup = keyboard.get_cancel_menu()
    ret = {'text': response,
           'markup': markup,
           }
    return ret


def handle_text(message, state: str) -> dict:
    global mess, user_id, status
    mess = message
    status = state
    user_id = message.from_user.id
    # Если Бог есть то эта функция - часть его
    stat = {'ready': start
            }
    response = stat[state]()

    return response
