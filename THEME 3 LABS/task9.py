def task2():
    salary = 5000  # зарплата
    spend = 6000  # траты
    months = 10  # количество месяцев
    increase = 0.03  # рост цен
    need_money = 0  # количество денег, чтобы прожить 10 месяцев

    while months > 0:
        need_money += (salary - spend)
        if months == 10:
            spend = spend
        else:
            spend *= increase
        months -= 1
    return need_money

print(task2())