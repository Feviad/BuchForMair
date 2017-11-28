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



def det_balance() -> float:
    query = f'SELECT value FROM income ' \
            f'WHERE id>0'
    incomes = query_req(query, True)
    income = 0
    for val in incomes:
        income = income + float(val[0])
    query = f'SELECT value FROM costs ' \
            f'WHERE id>0'
    costes = query_req(query, True)
    cost = 0
    for val in costes:
        cost = cost + float(val[0])
    return income - cost