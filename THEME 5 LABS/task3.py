from random import sample
n = 15
ynik = [i for i in range(-10, 11)]


def get_unique_list_numbers() -> list[int]:
    # TODO написать функцию для получения списка уникальных целых чисел
    return sample(ynik, n)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))