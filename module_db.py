import psycopg2

import settings


def query_sender(query: str) -> None:
    with psycopg2.connect(settings.DB_CONN) as conn:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()


def query_req(query: str, flag: bool) -> list:
    with psycopg2.connect(settings.DB_CONN) as conn:
        cur = conn.cursor()
        cur.execute(query)
        if flag:
            info = cur.fetchall()
        else:
            info = cur.fetchone()
        return info


def access_check(requester: int) -> bool:
     return requester in settings.access


def get_state(user_id: int) -> str:
    query = f'SELECT state FROM states ' \
            f'WHERE id={user_id}'
    return query_req(query, False)[0]

def new_state(user_id: int, new_state: str) -> None:
    query = f'UPDATE states ' \
            f'SET state = \'{new_state}\' ' \
            f'WHERE id = {user_id}'
    query_sender(query)

def get_balance(cash_id: int) -> float:
    query = f'SELECT SUM(sum) as income ' \
            f'FROM remittance ' \
            f'WHERE income = {cash_id}'
    income = query_req(query, False)[0]
    if income is None:
        income = 0
    else:
        income = income
    query = f'SELECT SUM(sum) as outgo ' \
            f'FROM remittance ' \
            f'WHERE outgo = {cash_id}'
    cost = query_req(query, False)[0]
    if cost is None:
        cost = 0
    else:
        cost = cost
    return income - cost

def get_cash_list() -> list:
    query = f'SELECT id, name FROM accounts'
    ret = []
    cash_desks = query_req(query, True)
    for cash in cash_desks:
        cash_dict = {'name': cash[1],
                     'balance': get_balance(int(cash[0]))
                     }
        ret.append(cash_dict)
    return ret