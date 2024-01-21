from src.func import sort_by_ex, sort_by_date, format_card, format_date, format_accaunt


test_list = [
    {
        "state": "EXEC",
        "date": "2019-07-03T18:35:29.512364"
    }, {
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041"}
]


def test_sort_by_ex():
    '''
    тест функции sort_by_ex
    которая сортирует список по ключу "EXECUTED"
    '''
    assert sort_by_ex(test_list) == [
        {"state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041"}]


def test_sort_by_date():
    '''
    тест функции sort_by_date
    которая сортирует список ключу "date"
    '''
    assert sort_by_date(test_list) == [
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"},
        {
            "state": "EXEC",
            "date": "2019-07-03T18:35:29.512364"}]


def test_format_accaunt():
    '''
    тест функции format_operation
    которая принимает строку
    выводит зашифрованный номер карты/счета
    '''
    assert format_accaunt("75106830613657916952") == "**6952"


def test_format_card():
    """
    тест функции format_card
    которя шифрует номер карты
    """
    assert format_card("7158300734726758") == "7158 30** **** 6758"


def test_format_date():
    '''
    тест функции format_date
    которая меняет формат даты
    '''
    assert format_date("2018-03-23T10:45:06.972075") == "23-03-2018"


