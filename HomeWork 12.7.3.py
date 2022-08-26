d = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

list_percent = list(d.values())
max_percent = max(list_percent)

print("Список банков", "||".join(d.keys()))
print ("Процентные ставки банков",list_percent)

deposit = input("Введите сумму, которую планируете положить под проценты: ")
list_deposit = list_percent.copy()
for i in range(len(list_deposit)):
    list_deposit[i] = float(deposit)* (1+list_percent[i]/100)

print ("Накопленные средства за год вклада в каждом из банков", list_deposit)
print("Максимальный банковский процент:", str(max_percent))
deposit_max = float(deposit)*(1+max_percent/100)
print ("Максимальная сумма, которую вы можете заработать за год:", str(deposit_max))