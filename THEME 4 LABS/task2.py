from pprint import pprint


def get_count_char(str_) -> dict:
    dict_t = {}
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    for symbol in str_.lower():
        if dict_t.get(symbol):
            dict_t[symbol] += 1
        else:
            dict_t |= {symbol: 1}
    return dict_t


def get_letter_percentage(dict_, char, summ_mass):
    return dict_[char] / summ_mass * 100


def get_percent_char(dict_) -> dict:
    dict_t = {}
    summ_mass = 0
    for key, value in dict_.items(): summ_mass += value
    for key, value in dict_.items():
        dict_t[key] = get_letter_percentage(dict_, key, summ_mass)
    return dict_t


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
pprint(get_count_char(main_str))
pprint(get_percent_char(get_count_char(main_str)))