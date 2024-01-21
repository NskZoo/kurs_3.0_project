import json
from datetime import datetime
def load_operations():
    '''
    функция которая загружает список операций
    '''
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)


def sort_by_ex(operation_list: list) -> list:
    '''
    функция которая сортирует список по ключу "EXECUTED"
    '''
    ex_list = []
    for n in operation_list:
        if n.get("state") == "EXECUTED":
            ex_list.append(n)
    return ex_list


def sort_by_date(operation_list: list) -> list:
    '''
    функция которая сортирует список ключу "date"
    '''
    return sorted(operation_list,key=lambda x: x["date"], reverse=True)


def format_card(card_number: str) -> str:
    '''
    функция которя шифрует номер карты
        '''
    if not len(card_number) == 16:
        raise ValueError('Card number must contain exactly 16 characters')


    start, middle, end = card_number[:6], card_number[6:-4], card_number[-4:]
    safe_card_number = start + '*' * len(middle) + end


    block_sizes = (4, 4, 4, 4)
    result = []
    for bs in block_sizes:
        block, tail = safe_card_number[:bs], safe_card_number[bs:]
        result.append(block)
        safe_card_number = tail

    return ' '.join(result)


def format_accaunt(account_number):
    """
    функция которя шифрует номер счёта
    """
    return '*' * 2 + account_number[-4:]

def format_date(iso_date):
    '''
    функция которая меняет формат даты
    '''
    item = datetime.fromisoformat(iso_date)
    new_date = item.strftime("%d-%m-%Y")
    return new_date



