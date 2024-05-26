per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Введите сумму, которую планируете положить под проценты: "))

# Список накопленных средств за год вклада в каждом из банков
deposit = [money * (rate / 100) for rate in per_cent.values()]
int_list = [int(element) for element in deposit]

# Преобразование списка float в список int
deposit_int = [int(d) for d in int_list]

# Поиск максимального значения в списке deposit_int
max_deposit = max(deposit_int)

print(int_list)
print(f"Максимальная сумма, которую вы можете заработать — {max_deposit}")