tickets = int(input("Введите количество приобретаемых билетов: "))
guests = tickets
sum = 0

while guests != 0:
    age_guest = int(input(f'Укажите возраст посетителя {guests}: '))
    if age_guest < 18:
        print('Билет бесплатный')
    elif 18 <= age_guest < 25:
        sum = sum + 990
        print('Стоимость билета: 990 руб.')
    elif 25 <= age_guest < 100:
        sum = sum + 1390
        print('Стоимость билета: 1390 руб.')
    else:
        print('Неверные данные возраста. Введи возраст повторно: ')
        continue
    guests = guests - 1

if tickets >= 3:
    sale = int(sum - sum / 10)
    print(f'Сумма к оплате {sale} руб., с учётом скидки в 10% за приобретение трёх и более билетов')
else:
    print(f'Сумма к оплате {sum} руб.')