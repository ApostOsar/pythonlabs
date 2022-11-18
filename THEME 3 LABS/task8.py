money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05



# TODO Оформить решение
def task(money_capital: float, salary: float, spend:float, increase: any) -> float:
    month = 0
    while money_capital > 0:
        money_capital +=(salary-spend)
        spend*= increase
        month +=1
    return month


print(task(money_capital,salary,spend,increase))
