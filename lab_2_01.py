money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital + salary >= spend:
    if month < 1:

        traty = money_capital + salary - spend
        money_capital = traty
        month += 1
    else:

        traty = money_capital + salary - (spend * (increase + 1))
        money_capital = traty
        spend = spend * (increase + 1)
        month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)

