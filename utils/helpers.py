import requests


from data import config


def count_openbid(some):
    i = 0
    for s in some['requests']:
        if s['status']['name'] == 'Открыто' \
                or s['status']['name'] == 'Утверждается' \
                or s['status']['name'] == 'Назначено':
            i += 1
    return f"открытых заявок: {i}"


def return_address_on_id_inc(text):
    bid = requests.get(url=config.url + {text}, headers=config.headers).json()
    return bid["request"]['udf_fields']['udf_sline_301']


def change_status_name(text):
    if text == 'Открыто':
        return 'О'
    elif text == 'Утверждается':
        return 'У'
    elif text == 'Закрыто':
        return 'З'
