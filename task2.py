# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

import decimal

names_list = ['Иван', 'Андрей', 'Дмитрий']
staff_list = [50_000, 20_000, 45_000]
bonus_list = ['10.25%', '1.23%', '9.99%']

def money(names_list: list[str], staff_list: list[int], bonus_list: list[str]) -> dict[str, decimal.Decimal]:
    return {name: sale / 100 * bon for name, sale, bon in zip(names_list, staff_list, (float(i[:-1]) for i in
    bonus_list))}.items()


print(*(money(names_list, staff_list, bonus_list)))

