general_price = 0
while True:
    try:
        ticket_number = input("Какое количество билетов Вы желаете приобрести?")
        ticket_number = int(ticket_number)
        if type(ticket_number) == int:
            break
    except ValueError:
        print("Введите количества билетов целым числом!")
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age = input(f'Билет №{i} для какого возраста? ')
            age = int(age)
            if (age < 18):
                print("Вы можете пройти бесплатно!")
            elif (age >= 18) and (age < 25):
                general_price += 990
                print("Стоимость билета составляет - 990 рублей")
            else:
                general_price += 1390
                print("Стоимость билета составляет - 1390 рублей")
            if type(age) == int:
                break
        except ValueError:
            print('Введите Ваш возраст целым числом!')
if ticket_number > 3:
    general_price = general_price - ((general_price / 100) * 10)
    print(f'Итого к оплате {general_price} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию более 3-х человек')
else:
    print(f'Итого к оплате {general_price} руб.')








