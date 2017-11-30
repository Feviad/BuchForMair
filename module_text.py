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
    response = 'Клавиатурой то пользуйся'
    markup = False
    ret = {'text': response,
           'markup': markup,
           }
    return ret

def return_to_main() -> dict:
    response = 'Возвращаемся в основное меню'
    markup = keyboard.get_main_menu()
    db.new_state(user_id, 'ready')
    ret = {'text': response,
           'markup': markup,
           }
    return ret


# =========================================================================== #
def start() -> dict:
    commands = {'Баланс': start_balance,
                'Заказы': start_orders
                }
    return commands.get(mess.text, error_text)()

def start_balance() -> dict:
    balance = db.get_balance(1)
    db.new_state(user_id, 'balance_menu')
    response = f'Касса фирмы: {balance}'
    markup = keyboard.get_balance_menu()
    ret = {'text': response,
           'markup': markup,
           }
    return ret


def start_orders() -> dict:
    # balance = db.get_balance(1)
    db.new_state(user_id, 'orders_menu')
    response = f'ORDERS'
    markup = keyboard.get_back_menu()
    ret = {'text': response,
           'markup': markup,
           }
    return ret
# =========================================================================== #


# =========================================================================== #
def balance_menu():
    commands = {'Счета': balance_cash,
                'Касса': error_text,
                'Назад': return_to_main
                }
    return commands.get(mess.text, error_text)()


def balance_cash():
    cash_desks = db.get_cash_list()
    response = ''
    for cash in cash_desks:
        name = cash['name']
        balance = cash['balance']
        line = f'{name}: {balance}\n'
        response = response + line
    markup = keyboard.get_back_menu()
    ret = {'text': response,
           'markup': markup,
           }
    return ret
# =========================================================================== #



def orders_menu() ->dict:
    commands = {
                'Назад': return_to_main
                }
    return commands.get(mess.text, error_text)()



def handle_text(message, state: str) -> dict:
    global mess, user_id, status
    mess = message
    status = state
    user_id = message.from_user.id
    # Если Бог есть то эта функция - часть его
    stat = {'ready': start,
            #
            'balance_menu': balance_menu,
                #
                'check_cash_menu': error_text,
                'invent': error_text,
            #
            'orders_menu': orders_menu,
                #
                'goods_menu': error_text,
                'couriers_menu': error_text,
                'clients_menu': error_text,
                    #
                    'new_order': error_text
            }
    response = stat[state]()

    return response
