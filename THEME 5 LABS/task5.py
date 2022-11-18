from random import sample


n = 8
syb = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz0123456789'


def get_random_password() -> str:
    # TODO написать функцию генерации случайных паролей
    return "".join(sample(syb, n))

print(get_random_password())